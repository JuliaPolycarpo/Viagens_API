from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario_model import Usuario
from app.Schema.usuario_schema import UsuarioCreate, UsuarioResponse

router = APIRouter(prefix="/usuarios", tags=["usuarios"]) #prefix serve para criar uma "pasta" para 
# as rotas, como se fosse as abas de um site

#Criar Usuario
@router.post("/", response_model=UsuarioResponse)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    novo_usuario = Usuario( 
        nome=usuario.nome,
        cpf=usuario.cpf,
        data_nascimento=usuario.data_nascimento,
        email=usuario.email,
        username=usuario.username,
        senha=usuario.senha )
    
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario


#Listar Usuarios 
@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()


#Buscar Usuario por ID
@router.get("/{id}", response_model=UsuarioResponse)
def buscar_usuario(id: int, db: Session = Depends(get_db)):
    return db.query(Usuario).filter(Usuario.id_usuario == id).first()


#Atualizar Usuario
@router.put("/{id}", response_model=UsuarioResponse)
def update_usuario(id: int, dados: UsuarioCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(usuario, campo, valor)

    db.commit()
    db.refresh(usuario)
    return usuario


#Deletar Usuario
@router.delete("/{id}")
def deletar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id).first()
    
    db.delete(usuario)
    db.commit()
    return {"msg": "Usuário deletado"}

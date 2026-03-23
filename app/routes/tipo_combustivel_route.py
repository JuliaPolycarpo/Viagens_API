from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipo_combustivel_model import TipoCombustivel
from app.Schema.tipo_combustivel_schema import TipoCombustivelBase, TipoCombustivelResponse

router = APIRouter(prefix="/tipos-combustivel", tags=["tipos_combustivel"])


# Criar Tipo de Combustível
@router.post("/", response_model=TipoCombustivelResponse)
def criar_tipo_combustivel(dados: TipoCombustivelBase, db: Session = Depends(get_db)):
    novo = TipoCombustivel(**dados.model_dump())

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


# Listar Tipos de Combustível
@router.get("/", response_model=list[TipoCombustivelResponse])
def listar_tipos_combustivel(db: Session = Depends(get_db)):
    return db.query(TipoCombustivel).all()


# Buscar por ID
@router.get("/{id}", response_model=TipoCombustivelResponse)
def buscar_tipo_combustivel(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoCombustivel).filter(TipoCombustivel.id_tipo_combustivel == id).first()

    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de combustível não encontrado")

    return tipo


# Atualizar
@router.put("/{id}", response_model=TipoCombustivelResponse)
def atualizar_tipo_combustivel(id: int, dados: TipoCombustivelBase, db: Session = Depends(get_db)):
    tipo = db.query(TipoCombustivel).filter(TipoCombustivel.id_tipo_combustivel == id).first()

    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de combustível não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(tipo, campo, valor)

    db.commit()
    db.refresh(tipo)
    return tipo


# Deletar
@router.delete("/{id}")
def deletar_tipo_combustivel(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoCombustivel).filter(TipoCombustivel.id_tipo_combustivel == id).first()

    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de combustível não encontrado")

    db.delete(tipo)
    db.commit()
    return {"msg": "Tipo de combustível deletado"}

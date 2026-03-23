from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.servico_model import Servico
from app.Schema.servico_schema import ServicoBase, ServicoResponse

router = APIRouter(prefix="/servicos", tags=["servicos"])

#Criar
@router.post("/", response_model=ServicoResponse)
def criar(dados: ServicoBase, db: Session = Depends(get_db)):
    novo = Servico(**dados.model_dump())
    
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


#Listar
@router.get("/", response_model=list[ServicoResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(Servico).all()


#Buscar po id
@router.get("/{id}", response_model=ServicoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    serviço = db.query(Servico).filter(Servico.id_servico == id).first()
    
    if not serviço:
        raise HTTPException(404, "Serviço não encontrado")
    
    return serviço

#Atualizar 
@router.put("/{id}", response_model=ServicoResponse)
def atualizar(id: int, dados: ServicoBase, db: Session = Depends(get_db)):
    serviço = db.query(Servico).filter(Servico.id_servico == id).first()
    
    if not serviço:
        raise HTTPException(404, "Serviço não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(serviço, campo, valor)

    db.commit()
    db.refresh(serviço)
    return serviço


#deletar
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    serviço = db.query(Servico).filter(Servico.id_servico == id).first()
    
    if not serviço:
        raise HTTPException(404, "Serviço não encontrado")

    db.delete(serviço)
    db.commit()
    return {"msg": "Serviço deletado"}
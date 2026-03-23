from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.passageiro_model import Passageiro
from app.Schema.passageiro_schema import PassageiroBase, PassageiroResponse

router = APIRouter(prefix="/passageiros", tags=["passageiros"])

#Criar
@router.post("/", response_model=PassageiroResponse)
def criar(dados: PassageiroBase, db: Session = Depends(get_db)):
    novo = Passageiro(**dados.model_dump())
    
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


#Listar
@router.get("/", response_model=list[PassageiroResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(Passageiro).all()


#Buscar por ID
@router.get("/{id}", response_model=PassageiroResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    passageiro = db.query(Passageiro).filter(Passageiro.id_passageiro == id).first()
   
    if not passageiro:
        raise HTTPException(404, "Passageiro não encontrado")
    
    return passageiro


# Atualizar Passageiro
@router.put("/{id}", response_model=PassageiroResponse)
def update_passageiro(id: int, dados: PassageiroBase, db: Session = Depends(get_db)):
    passageiro = db.query(Passageiro).filter(Passageiro.id_passageiro == id).first()

    if not passageiro:
        raise HTTPException(404, "Passageiro não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(passageiro, campo, valor)

    db.commit()
    db.refresh(passageiro)
    return passageiro


#Delete
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    passageiro = db.query(Passageiro).filter(Passageiro.id_passageiro == id).first()

    if not passageiro:
        raise HTTPException(404, "Passageiro não encontrado")

    db.delete(passageiro)
    db.commit()
    return {"msg": "Passageiro deletado"}
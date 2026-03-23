from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista_model import Motorista
from app.Schema.motorista_schema import MotoristaBase, MotoristaResponse

router = APIRouter(prefix="/motoristas", tags=["motoristas"])

#Criar
@router.post("/", response_model=MotoristaResponse)
def criar(dados: MotoristaBase, db: Session = Depends(get_db)):
    novo = Motorista(**dados.model_dump())
    
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

#Listar
@router.get("/", response_model=list[MotoristaResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(Motorista).all()

#Buscar por ID
@router.get("/{id}", response_model=MotoristaResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    motorista = db.query(Motorista).filter(Motorista.id_motorista == id).first()
    
    if not motorista:
        raise HTTPException(404, "Motorista não encontrado")
    
    return motorista

# Atualizar Motorista
@router.put("/{id}", response_model=MotoristaResponse)
def atualizar(id: int, dados: MotoristaBase, db: Session = Depends(get_db)):
    motorista = db.query(Motorista).filter(Motorista.id_motorista == id).first()
    
    if not motorista:
        raise HTTPException(404, "Motorista não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(motorista, campo, valor)

    db.commit()
    db.refresh(motorista)
    return motorista

# Deletar Motorista 
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    motorista = db.query(Motorista).filter(Motorista.id_motorista == id).first()

    if not motorista:
        raise HTTPException(404, "Motorista não encontrado")

    db.delete(motorista)
    db.commit()
    return {"msg": "Motorista deletado"}

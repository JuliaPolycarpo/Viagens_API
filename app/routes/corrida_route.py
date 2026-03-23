from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.corrida_model import Corrida
from app.Schema.corrida_schema import CorridaBase, CorridaResponse

router = APIRouter(prefix="/corridas", tags=["corridas"])


# Criar Corrida
@router.post("/", response_model=CorridaResponse)
def criar_corrida(dados: CorridaBase, db: Session = Depends(get_db)):
    novo = Corrida(**dados.model_dump())

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


# Listar Corridas
@router.get("/", response_model=list[CorridaResponse])
def listar_corridas(db: Session = Depends(get_db)):
    return db.query(Corrida).all()


# Buscar por ID
@router.get("/{id}", response_model=CorridaResponse)
def buscar_corrida(id: int, db: Session = Depends(get_db)):
    corrida = db.query(Corrida).filter(Corrida.id_corrida == id).first()

    if not corrida:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")

    return corrida


# Atualizar Corrida
@router.put("/{id}", response_model=CorridaResponse)
def atualizar_corrida(id: int, dados: CorridaBase, db: Session = Depends(get_db)):
    corrida = db.query(Corrida).filter(Corrida.id_corrida == id).first()

    if not corrida:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(corrida, campo, valor)

    db.commit()
    db.refresh(corrida)
    return corrida


# Deletar Corrida
@router.delete("/{id}")
def deletar_corrida(id: int, db: Session = Depends(get_db)):
    corrida = db.query(Corrida).filter(Corrida.id_corrida == id).first()

    if not corrida:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")

    db.delete(corrida)
    db.commit()
    return {"msg": "Corrida deletada"}
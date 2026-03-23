from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.avaliacao_model import Avaliacao
from app.Schema.avaliacao_schema import AvaliacaoBase, AvaliacaoResponse

router = APIRouter(prefix="/avaliacoes", tags=["avaliacoes"])


# Criar Avaliação
@router.post("/", response_model=AvaliacaoResponse)
def criar_avaliacao(dados: AvaliacaoBase, db: Session = Depends(get_db)):
    novo = Avaliacao(**dados.model_dump())

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


# Listar Avaliaçao
@router.get("/", response_model=list[AvaliacaoResponse])
def listar_avaliacoes(db: Session = Depends(get_db)):
    return db.query(Avaliacao).all()


# Buscar por ID
@router.get("/{id}", response_model=AvaliacaoResponse)
def buscar_avaliacao(id: int, db: Session = Depends(get_db)):
    avaliaçao = db.query(Avaliacao).filter(Avaliacao.id_avaliacao == id).first()

    if not avaliaçao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    return avaliaçao


# Atualizar Avaliação
@router.put("/{id}", response_model=AvaliacaoResponse)
def atualizar_avaliacao(id: int, dados: AvaliacaoBase, db: Session = Depends(get_db)):
    avaliaçao = db.query(Avaliacao).filter(Avaliacao.id_avaliacao == id).first()

    if not avaliaçao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(avaliaçao, campo, valor)

    db.commit()
    db.refresh(avaliaçao)
    return avaliaçao


# Deletar Avaliação
@router.delete("/{id}")
def deletar_avaliacao(id: int, db: Session = Depends(get_db)):
    avaliaçao = db.query(Avaliacao).filter(Avaliacao.id_avaliacao == id).first()

    if not avaliaçao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    db.delete(avaliaçao)
    db.commit()
    return {"msg": "Avaliação deletada"}
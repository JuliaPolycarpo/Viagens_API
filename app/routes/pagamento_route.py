from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pagamento_model import Pagamento
from app.Schema.pagamento_schema import PagamentoBase, PagamentoResponse

router = APIRouter(prefix="/pagamentos", tags=["pagamentos"])


# Criar Pagamento
@router.post("/", response_model=PagamentoResponse)
def criar_pagamento(dados: PagamentoBase, db: Session = Depends(get_db)):
    novo = Pagamento(**dados.model_dump())

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


# Listar Pagamentos
@router.get("/", response_model=list[PagamentoResponse])
def listar_pagamentos(db: Session = Depends(get_db)):
    return db.query(Pagamento).all()


# Buscar por ID
@router.get("/{id}", response_model=PagamentoResponse)
def buscar_pagamento(id: int, db: Session = Depends(get_db)):
    pagamento = db.query(Pagamento).filter(Pagamento.id_pagamento == id).first()

    if not pagamento:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")

    return pagamento


# Atualizar Pagamento
@router.put("/{id}", response_model=PagamentoResponse)
def atualizar_pagamento(id: int, dados: PagamentoBase, db: Session = Depends(get_db)):
    pagamento = db.query(Pagamento).filter(Pagamento.id_pagamento == id).first()

    if not pagamento:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(pagamento, campo, valor)

    db.commit()
    db.refresh(pagamento)
    return pagamento


# Deletar Pagamento
@router.delete("/{id}")
def deletar_pagamento(id: int, db: Session = Depends(get_db)):
    pagamento = db.query(Pagamento).filter(Pagamento.id_pagamento == id).first()

    if not pagamento:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")

    db.delete(pagamento)
    db.commit()
    return {"msg": "Pagamento deletado"}
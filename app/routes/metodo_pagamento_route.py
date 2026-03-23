from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.metodo_pagamento_model import MetodoPagamento
from app.Schema.metodo_pagamento_schema import MetodoPagamentoBase, MetodoPagamentoResponse

router = APIRouter(prefix="/metodos-pagamento", tags=["metodos_pagamento"])


#Criar
@router.post("/", response_model=MetodoPagamentoResponse)
def criar(dados: MetodoPagamentoBase, db: Session = Depends(get_db)):
    novo = MetodoPagamento(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


#Listar
@router.get("/", response_model=list[MetodoPagamentoResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(MetodoPagamento).all()


#Buscar id
@router.get("/{id}", response_model=MetodoPagamentoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    pagamento = db.query(MetodoPagamento).filter(MetodoPagamento.id_metodo_pagamento == id).first()
    
    if not pagamento:
        raise HTTPException(404, "Não encontrado")
    
    return pagamento


#Atualizar
@router.put("/{id}", response_model=MetodoPagamentoResponse)
def atualizar(id: int, dados: MetodoPagamentoBase, db: Session = Depends(get_db)):
    pagamento = db.query(MetodoPagamento).filter(MetodoPagamento.id_metodo_pagamento == id).first()
    
    if not pagamento:
        raise HTTPException(404, "Metodo pagamento não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(pagamento, campo, valor)

    db.commit()
    db.refresh(pagamento)
    return pagamento


#Deletar
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    pagamento = db.query(MetodoPagamento).filter(MetodoPagamento.id_metodo_pagamento == id).first()
    
    if not pagamento:
        raise HTTPException(404, "Metodo pagamento não encontrado")

    db.delete(pagamento)
    db.commit()
    return {"msg": "Metodo pagamento deletado"}
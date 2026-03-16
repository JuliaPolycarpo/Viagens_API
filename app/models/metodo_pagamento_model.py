from sqlalchemy import Column, Integer, String
from app.database import Base


class MetodoPagamento(Base):
    __tablename__ = "metodo_pagamento"

    id_metodo_pagamento = Column(Integer, primary_key=True)
    descricao = Column(String(45))
    nome_financeira = Column(String(45))
from sqlalchemy import Column, Integer, String, DECIMAL
from app.database import Base


class TipoCombustivel(Base):
    __tablename__ = "tipo_combustivel"

    id_tipo_combustivel = Column(Integer, primary_key=True)
    descricao = Column(String(45))
    fator_carbono = Column(DECIMAL(10,5))
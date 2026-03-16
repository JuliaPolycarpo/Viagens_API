from sqlalchemy import Column, BigInteger, DECIMAL, DateTime
from app.database import Base


class Avaliacao(Base):
    __tablename__ = "avaliacao"

    id_avaliacao = Column(BigInteger, primary_key=True)
    nota_passageiro = Column(DECIMAL(3,2))
    nota_motorista = Column(DECIMAL(3,2))
    datahora_limite = Column(DateTime)
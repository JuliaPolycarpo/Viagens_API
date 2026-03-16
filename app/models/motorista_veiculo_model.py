from sqlalchemy import Column, BigInteger, Integer, DateTime, ForeignKey
from app.database import Base


class MotoristaVeiculo(Base):
    __tablename__ = "motorista_veiculo"

    id_motorista = Column(
        BigInteger,
        ForeignKey("motorista.id_motorista"),
        primary_key=True
    )

    id_veiculo = Column(
        Integer,
        ForeignKey("veiculo.id_veiculo"),
        primary_key=True
    )

    datahora_inicio_disponibilidade = Column(DateTime)
    datahora_fim_disponibilidade = Column(DateTime)
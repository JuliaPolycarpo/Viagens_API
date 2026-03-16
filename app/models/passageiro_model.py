from sqlalchemy import Column, BigInteger, ForeignKey, DECIMAL
from app.database import Base


class Passageiro(Base):
    __tablename__ = "passageiro"

    id_passageiro = Column(BigInteger, primary_key=True)
    id_usuario = Column(BigInteger, ForeignKey("usuario.id_usuario"))
    media_avaliacao = Column(DECIMAL(3,2))
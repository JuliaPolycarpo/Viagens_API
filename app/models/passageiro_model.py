from sqlalchemy import Column, BigInteger, ForeignKey, String, DECIMAL
from app.database import Base


class Passageiro(Base):
    __tablename__ = "passageiro"

    nome_passageiro = Column(String(255))
    id_passageiro = Column(BigInteger, primary_key=True)
    id_usuario = Column(BigInteger, ForeignKey("usuario.id_usuario"))
    media_avaliacao = Column(DECIMAL(3,2))
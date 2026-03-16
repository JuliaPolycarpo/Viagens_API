from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class ModeloVeiculo(Base):
    __tablename__ = "modelo_veiculo"

    id_modelo_veiculo = Column(Integer, primary_key=True)
    nome_modelo = Column(String(45))
    fabricante = Column(String(45))
    cor = Column(String(45))
    ano = Column(Integer)
    capacidade = Column(Integer)
    propriedade = Column(String(20))

    id_tipo_combustivel = Column(
        Integer,
        ForeignKey("tipo_combustivel.id_tipo_combustivel")
    )
from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Veiculo(Base):
    __tablename__ = "veiculo"

    id_veiculo = Column(Integer, primary_key=True)
    placa = Column(String(7))

    id_modelo_veiculo = Column(
        Integer,
        ForeignKey("modelo_veiculo.id_modelo_veiculo")
    )

    tem_seguro = Column(Integer)

    id_classe_veiculo = Column(
        Integer,
        ForeignKey("classe_veiculo.id_classe_veiculo")
    )
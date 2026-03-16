from sqlalchemy import Column, Integer, String, DECIMAL
from app.database import Base


class ClasseVeiculo(Base):
    __tablename__ = "classe_veiculo"

    id_classe_veiculo = Column(Integer, primary_key=True)
    nome_classe = Column(String(45))
    fator_preco = Column(DECIMAL(10,2))
from pydantic import BaseModel

class ClasseVeiculoBase(BaseModel):
    nome_classe: str
    fator_preco: float

class ClasseVeiculoCreate(ClasseVeiculoBase):
    pass

class ClasseVeiculoResponse(ClasseVeiculoBase):
    id_classe_veiculo: int

    class Config:
        from_attributes = True
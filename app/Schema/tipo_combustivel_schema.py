from pydantic import BaseModel


class TipoCombustivelBase(BaseModel):
    descricao: str
    fator_carbono: float
    id_tipo_combustivel: int

    class Config:
        from_attributes = True
from xmlrpc.client import boolean

from pydantic import BaseModel


class VeiculoBase(BaseModel):
    placa: str
    id_modelo_veiculo: int
    tem_seguro: bool
    id_classe_veiculo: int


class VeiculoResponse(VeiculoBase):
    id_veiculo: int

    class Config:
        from_attributes = True
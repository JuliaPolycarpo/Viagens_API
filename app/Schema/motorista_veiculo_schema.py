from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MotoristaVeiculoBase(BaseModel):
    id_motorista: int
    id_veiculo: int
    datahora_inicio_disponibilidade: Optional[datetime]
    datahora_fim_disponibilidade: Optional[datetime]

class MotoristaVeiculoCreate(MotoristaVeiculoBase):
    pass

class MotoristaVeiculoResponse(MotoristaVeiculoBase):

    class Config:
        from_attributes = True
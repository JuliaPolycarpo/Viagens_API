from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CorridaBase(BaseModel):
    id_passageiro: int
    id_motorista: int
    id_servico: int
    id_avaliacao: Optional[int]

    datahora_inicio: datetime
    datahora_fim: Optional[datetime]

    duracao_total: float
    gps_local_partida: str
    gps_local_destino: str

    valor_estimado: float
    status: str


class CorridaCreate(CorridaBase):
    pass


class CorridaResponse(CorridaBase):
    id_corrida: int

    class Config:
        from_attributes = True
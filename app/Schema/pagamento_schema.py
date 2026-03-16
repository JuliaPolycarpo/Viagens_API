from pydantic import BaseModel
from datetime import datetime


class PagamentoBase(BaseModel):
    id_corrida: int
    valor: float
    id_metodo_pagamento: int
    datahora_transacao: datetime


class PagamentoCreate(PagamentoBase):
    pass


class PagamentoResponse(PagamentoBase):
    id_pagamentos: int

    class Config:
        from_attributes = True
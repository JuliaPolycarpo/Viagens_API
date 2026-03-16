from pydantic import BaseModel

class MetodoPagamentoBase(BaseModel):
    descricao: str
    nome_financeira: str

class MetodoPagamentoCreate(MetodoPagamentoBase):
    pass

class MetodoPagamentoResponse(MetodoPagamentoBase):
    id_metodo_pagamento: int

    class Config:
        from_attributes = True
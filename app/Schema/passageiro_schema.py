from pydantic import BaseModel
from typing import Optional


class PassageiroBase(BaseModel):
    id_usuario: int
    media_avaliacao: Optional[float]


class PassageiroCreate(PassageiroBase):
    pass


class PassageiroResponse(PassageiroBase):
    id_passageiro: int

    class Config:
        from_attributes = True
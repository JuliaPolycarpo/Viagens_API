from pydantic import BaseModel
from datetime import date


class UsuarioBase(BaseModel): #Oq eu preciso para criar um usuario
    nome: str
    cpf: str
    data_nascimento: date
    email: str
    username: str


class UsuarioCreate(UsuarioBase):
    senha: str


class UsuarioResponse(UsuarioBase): #Oq a API vai retornar para mim
    id_usuario: int

    class Config:
        from_attributes = True
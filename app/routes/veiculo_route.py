from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.veiculo_model import Veiculo
from app.Schema.veiculo_schema import VeiculoBase, VeiculoResponse

router = APIRouter(prefix="/veiculos", tags=["veiculos"])


#Criar veiculo
@router.post("/", response_model=VeiculoResponse)
def criar(dados: VeiculoBase, db: Session = Depends(get_db)):
    novo = Veiculo(**dados.model_dump())

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


#Listar 
@router.get("/", response_model=list[VeiculoResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(Veiculo).all()


#Buscar por id 
@router.get("/{id}", response_model=VeiculoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    veiculo = db.query(Veiculo).filter(Veiculo.id_veiculo == id).first()

    if not veiculo:
        raise HTTPException(404, "Veículo não encontrado")
    
    return veiculo


#Atualizar
@router.put("/{id}", response_model=VeiculoResponse)
def atualizar(id: int, dados: VeiculoBase, db: Session = Depends(get_db)):
    veiculo = db.query(Veiculo).filter(Veiculo.id_veiculo == id).first()

    if not veiculo:
        raise HTTPException(404, "Veículo não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(veiculo, campo, valor)

    db.commit()
    db.refresh(veiculo)
    return veiculo


#deletar
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    veiculo = db.query(Veiculo).filter(Veiculo.id_veiculo == id).first()
    
    if not veiculo:
        raise HTTPException(404, "Veículo não encontrado")

    db.delete(veiculo)
    db.commit()
    return {"msg": "Veículo deletado"}
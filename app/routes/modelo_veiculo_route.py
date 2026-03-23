from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.modelo_veiculo_model import ModeloVeiculo
from app.Schema.modelo_veiculo_schema import ModeloVeiculoBase, ModeloVeiculoResponse

router = APIRouter(prefix="/modelos-veiculo", tags=["modelos_veiculo"])


#Criar modelo
@router.post("/", response_model=ModeloVeiculoResponse)
def criar(dados: ModeloVeiculoBase, db: Session = Depends(get_db)):
    novo = ModeloVeiculo(**dados.model_dump())
    
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


#Listar modelo
@router.get("/", response_model=list[ModeloVeiculoResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(ModeloVeiculo).all()


#Buscar modelo por id 
@router.get("/{id}", response_model=ModeloVeiculoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    modelo = db.query(ModeloVeiculo).filter(ModeloVeiculo.id_modelo_veiculo == id).first()
    
    if not modelo:
        raise HTTPException(404, "Modelo não encontrado")
    
    return modelo


#Atualizar modelo
@router.put("/{id}", response_model=ModeloVeiculoResponse)
def atualizar(id: int, dados: ModeloVeiculoBase, db: Session = Depends(get_db)):
    modelo = db.query(ModeloVeiculo).filter(ModeloVeiculo.id_modelo_veiculo == id).first()
    
    if not modelo:
        raise HTTPException(404, "Modelo não encontrado")

    for campo, valor in dados.model_dump().items():
        setattr(modelo, campo, valor)

    db.commit()
    db.refresh(modelo)
    return modelo


#Deletar modelo
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    modelo = db.query(ModeloVeiculo).filter(ModeloVeiculo.id_modelo_veiculo == id).first()
    
    if not modelo:
        raise HTTPException(404, "Modelo não encontrado")

    db.delete(modelo)
    db.commit()
    return {"msg": "Modelo deletado"}
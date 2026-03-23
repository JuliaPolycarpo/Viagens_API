from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.classe_veiculo_model import ClasseVeiculo
from app.Schema.classe_veiculo_schema import ClasseVeiculoBase, ClasseVeiculoResponse

router = APIRouter(prefix="/classes-veiculo", tags=["classes_veiculo"])


# Criar Classe de Veículo
@router.post("/", response_model=ClasseVeiculoResponse)
def criar_classe_veiculo(dados: ClasseVeiculoBase, db: Session = Depends(get_db)):
    novo = ClasseVeiculo(**dados.model_dump())

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


# Listar Classes de Veículo
@router.get("/", response_model=list[ClasseVeiculoResponse])
def listar_classes_veiculo(db: Session = Depends(get_db)):
    return db.query(ClasseVeiculo).all()


# Buscar Classe por ID
@router.get("/{id}", response_model=ClasseVeiculoResponse)
def buscar_classe_veiculo(id: int, db: Session = Depends(get_db)):
    classe = db.query(ClasseVeiculo).filter(ClasseVeiculo.id_classe_veiculo == id).first()

    if not classe:
        raise HTTPException(status_code=404, detail="Classe de veículo não encontrada")

    return classe


# Atualizar Classe de Veículo
@router.put("/{id}", response_model=ClasseVeiculoResponse)
def atualizar_classe_veiculo(id: int, dados: ClasseVeiculoBase, db: Session = Depends(get_db)):
    classe = db.query(ClasseVeiculo).filter(ClasseVeiculo.id_classe_veiculo == id).first()

    if not classe:
        raise HTTPException(status_code=404, detail="Classe de veículo não encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(classe, campo, valor)

    db.commit()
    db.refresh(classe)
    return classe


# Deletar Classe de Veículo
@router.delete("/{id}")
def deletar_classe_veiculo(id: int, db: Session = Depends(get_db)):
    classe = db.query(ClasseVeiculo).filter(ClasseVeiculo.id_classe_veiculo == id).first()

    if not classe:
        raise HTTPException(status_code=404, detail="Classe de veículo não encontrada")

    db.delete(classe)
    db.commit()
    return {"msg": "Classe de veículo deletada"}
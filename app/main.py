from fastapi import FastAPI
from app.routes import usuario_route, passageiro_route,  motorista_route, motorista_veiculo_route, classe_veiculo_route, tipo_combustivel_route, modelo_veiculo_route, metodo_pagamento_route, veiculo_route, servico_route, avaliacao_route, corrida_route, pagamento_route
from app.database import engine, Base
from app.models.motorista_veiculo_model import MotoristaVeiculo

#MotoristaVeiculo.__table__.drop(bind=engine)
#MotoristaVeiculo.__table__.create(bind=engine)
#Base.metadata.drop_all(bind=engine) 
Base.metadata.create_all(bind=engine) 
app = FastAPI()

app.include_router(usuario_route.router)
app.include_router(tipo_combustivel_route.router)
app.include_router(classe_veiculo_route.router)
app.include_router(metodo_pagamento_route.router)
app.include_router(servico_route.router)
app.include_router(modelo_veiculo_route.router)
app.include_router(passageiro_route.router)
app.include_router(motorista_route.router)
app.include_router(veiculo_route.router)
app.include_router(motorista_veiculo_route.router)
app.include_router(corrida_route.router)
app.include_router(pagamento_route.router)
app.include_router(avaliacao_route.router)







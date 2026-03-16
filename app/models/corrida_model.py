from sqlalchemy import Column, BigInteger, Integer, String, DateTime, DECIMAL, ForeignKey
from app.database import Base


class Corrida(Base):
    __tablename__ = "corrida"

    id_corrida = Column(BigInteger, primary_key=True)

    id_passageiro = Column(BigInteger, ForeignKey("passageiro.id_passageiro"))
    id_motorista = Column(BigInteger, ForeignKey("motorista.id_motorista"))
    id_servico = Column(Integer, ForeignKey("servico.id_servico"))
    id_avaliacao = Column(BigInteger, ForeignKey("avaliacao.id_avaliacao"))

    datahora_inicio = Column(DateTime)
    datahora_fim = Column(DateTime)

    duracao_total = Column(DECIMAL(4,2))

    gps_local_partida = Column(String(50))
    gps_local_destino = Column(String(50))

    valor_estimado = Column(DECIMAL(10,2))
    status = Column(String(20))
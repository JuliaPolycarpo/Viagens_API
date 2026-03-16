from sqlalchemy import Column, BigInteger, Integer, DECIMAL, DateTime, ForeignKey
from app.database import Base


class Pagamento(Base):
    __tablename__ = "pagamento"

    id_pagamentos = Column(BigInteger, primary_key=True)

    id_corrida = Column(BigInteger, ForeignKey("corrida.id_corrida"))
    valor = Column(DECIMAL(10,2))

    id_metodo_pagamento = Column(
        Integer,
        ForeignKey("metodo_pagamento.id_metodo_pagamento")
    )

    datahora_transacao = Column(DateTime)
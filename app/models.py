from sqlalchemy import Column, Interger, String, Text, BigInterger, Index, UniqueConstraint
from .db import Base

class Record(Base):
    __tablename__ = "registros"
    id = Column(Interger, primary_key=True, autoincrement=True) #TICKET ID
    wa_id = Column(String(64), index=True, nullable=False)
    cedula = Column(String(16), index=True, nullable=False)
    placa = Column(String(16), index=True, nullable=True) #ABC123
    placa_original = Column(String(64), index=True, nullable=False) # Administracion | polizas_tarjetas_operacion | acuerdos_pago
    file_path = Column(Text, nullable=True)
    content_type = Column(String(64), nullable=True)
    file_size = Column(BigInterger, nullable=True)
    created_at = Column(BigInterger, index=True, nullable=False) #epoch
    estado = Column(String(32), nullable=False, default="nuevo")
    sheets_synced = Column(Interger, nullable=False, default=0) #0/1
Index("idx_registros_created_at", Record.created_at)
Index("idx_registros_compuesto", Record.cedula, Record.placa, Record.tipo_recibo)

class SessionState(Base):
    __tablename__ = "sessions"
    wa_id = Column(String(64), primary_key(True), autoincrement= True) #ticket_id
    state = Column(String(32), nullable=False)
    payload_json = Column(Text, nullable=False, default="{}")
    updated_at = Column(BigInterger, nullable=False)


class SheetsQueue(Base):
    __tablename__ = "sheets_queue"
    id = Column(Interger, primary_key=True, autoincrement=True)
    record_id = Column(Interger, nullable=False)
    try_count = Column(Interger, nullable=False, default=0)
    last_error = Column(Text, nullable=True)
    next_attempt_at = Column(BigInterger, nullable=False)
    __table_arg__ = (UniqueConstraint('record_id', name='uq_queue_records'),)



    

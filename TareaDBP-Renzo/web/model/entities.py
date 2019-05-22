from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class User(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    codigo = Column(Integer)
    nombre = Column(String(50))
    apellido = Column(String(50))
    password = Column(String(50))

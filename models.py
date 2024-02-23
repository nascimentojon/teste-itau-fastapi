from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
  __tablename__ = 'tb_users'

  id = Column(Integer, primary_key=True, index=True)
  nome_completo = Column(String(100), unique=True)
  cpf = Column(String(11), unique=True)
  endereco = Column(String(100))        
  data_nascimento = Column(String(100))        
  estado_civil = Column(String(100))        
        

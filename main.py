from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from pydantic import BaseModel
from typing import Annotated
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)



app = FastAPI ()

class UserBase(BaseModel):
  nome_completo: str
  cpf: str
  endereco: str
  data_nascimento: str
  estado_civil: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post('/usuarios/', status_code=status.HTTP_201_CREATED, tags=['usuarios'])
async def create_user(user: UserBase, db: db_dependency):
  db_user = models.User(**user.model_dump())
  db.add(db_user)
  db.commit()

@app.get("/usuarios/", status_code=status.HTTP_200_OK, tags=['usuarios'])
async def all_user( db: db_dependency):
  user = db.query(models.User).all()
  return user

@app.put("/usuarios/{user_id}", status_code=status.HTTP_200_OK, tags=['usuarios'])
async def update_user(user_id: int, db: db_dependency, user_data: dict):
    db_user = db.query(models.User).filter()
    if db_user is None:
      raise HTTPException(status_code=404, detail="user not found")
    
@app.delete('/usuarios/{user_id}', status_code=status.HTTP_200_OK, tags=['usuarios'])
async def delete_user(user_id: int, db: db_dependency):
  user = db.query(models.User).filter(models.User.id == user_id).first()
  if user is None:
    raise HTTPException(status_code=404, detail="user not found")
  db.delete(user)
  db.commit()
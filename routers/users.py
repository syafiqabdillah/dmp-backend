from fastapi import APIRouter, HTTPException
from typing import Optional 
from pydantic import BaseModel

import services.users as db

name = "users"

router = APIRouter(
  prefix=f"/{name}",
  tags=[name]
)

class FormUser(BaseModel):
  username: str
  password: str

@router.post('/register')
def register(form: FormUser):
  return db.register(form.username, form.password)

@router.post('/login')
def login(form: FormUser):
  return db.login(form.username, form.password)

@router.get('/')
def getAll():
  return db.getAll()
from fastapi import APIRouter, HTTPException
from typing import Optional 
from pydantic import BaseModel

import services.task as db

name = "task"

router = APIRouter(
  prefix=f"/{name}",
  tags=[name]
)

class FormCreate(BaseModel):
  dataset_url: str
  dataset_name: str
  created_by: str

@router.post('/', status_code=201)
def create(form: FormCreate):
  return db.create(form.dataset_url, form.dataset_name, form.created_by)

@router.get('/')
def getAll():
  return db.getAll()

@router.get('/available')
def getAvailable():
  return db.getAvailable()

class FormDelete(BaseModel):
  id: str
  deleted_by: str

@router.post('/delete')
def delete(form: FormDelete):
  return db.delete(form.id, form.deleted_by)

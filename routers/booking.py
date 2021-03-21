from fastapi import APIRouter, HTTPException
from typing import Optional
from pydantic import BaseModel

import services.booking as db

name = "booking"

router = APIRouter(
    prefix=f"/{name}",
    tags=[name]
)


class FormCreate(BaseModel):
    task_id: str
    created_by: str


@router.post('/', status_code=201)
def create(form: FormCreate):
    return db.create(form.task_id, form.created_by)


class FormRevoke(BaseModel):
    booking_id: str


@router.post('/revoke')
def revoke(form: FormRevoke):
    return db.revoke(form.booking_id)


@router.get('/by-user')
def getByUser(username: str):
    return db.getByUser(username)

@router.get('/count')
def getAll():
    return len(db.getAll())
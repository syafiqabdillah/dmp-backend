from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from utils.auth import generate_id
from routers import users, task, booking

app = FastAPI()

app.include_router(users.router)
app.include_router(task.router)
app.include_router(booking.router)

origins = [
  "http://localhost",
  "http://localhost:3000",
  "https://dmp-konvergenai.herokuapp.com/"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def home():
  return RedirectResponse("/docs")

@app.get('/token', description="Generate 256 chars random string")
def token():
  return generate_id(256)
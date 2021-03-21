from utils.executor import execute_get, execute_post
from utils.auth import get_current_time, hash_password, password_matches, create_jwt
from fastapi import HTTPException

def register(username, password):
  query = """
          INSERT INTO users (username, hashed_password, created_date)
          VALUES (%s, %s, %s)
          RETURNING username
          """
  created_date = get_current_time()
  hashed_password = hash_password(password)
  return execute_post(query, (username, hashed_password, created_date))

def login(username, password):
  query = """
          SELECT username, hashed_password
          FROM users
          WHERE username = %s
          """
  result = execute_get(query, (username, ))
  if len(result) > 0:
    username = result[0][0]
    hashed_password = result[0][1].encode()
    if password_matches(password, hashed_password):
      return _getJwt(username)
    else:
      raise HTTPException(status_code=403, detail="Unauthorized access")
  else:
    raise HTTPException(status_code=404, detail="Username not found")

def getByUsername(username):
  query = """
          SELECT username, created_date, active
          FROM users
          WHERE username = %s
          """
  result = execute_get(query, (username, ))[0]
  return {
    "username": result[0],
    "created_date": str(result[1]),
    "active": result[2]
  }

def getAll():
  query = """
          SELECT username, created_date, active
          FROM users 
          """
  results = execute_get(query, ())
  return [
    {
      "username": result[0],
      "created_date": result[1],
      "active": result[2]
    } for result in results
  ]

def _getJwt(username):
  user = getByUsername(username)
  jwt = create_jwt(user)
  return {
    "jwt": jwt
  }
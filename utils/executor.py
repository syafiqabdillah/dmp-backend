from dotenv import load_dotenv
from fastapi import HTTPException
import psycopg2
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')


def execute_get(query, val):
  try:
    connection = psycopg2.connect(
        user=DB_USER,
        host=DB_HOST,
        database=DB_NAME,
        password=DB_PASS,
    )
    cursor = connection.cursor()
    cursor.execute(query, val)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
  except Exception as e:
    print(e)
    raise HTTPException(status_code=500, detail='System error')


def execute_post(query, val):
  try:
    connection = psycopg2.connect(
      user=DB_USER,
      password=DB_PASS,
      host=DB_HOST,
      database=DB_NAME
    )
    cursor = connection.cursor()
    cursor.execute(query, val)
    connection.commit()
    returning_id = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return {
      'returning_id': returning_id
    }
  except Exception as e:
    print(e)
    raise HTTPException(status_code=500, detail='System error')

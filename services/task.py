from utils.executor import execute_get, execute_post
from utils.auth import get_current_time, generate_id
from fastapi import HTTPException


def getById(id):
    query = BASE + " WHERE id = %s"
    result = execute_get(query, (id, ))
    if len(result) > 0:
        result = result[0]
        return {
            "id": result[0],
            "dataset_url": result[1],
            "dataset_name": result[2],
            "created_by": result[3],
            "created_date": result[4],
            "deleted_by": result[5],
            "deleted_date": result[6],
        }
    else:
        raise HTTPException(404)


def getAll():
    query = BASE + " ORDER BY created_date desc"
    results = execute_get(query, ())
    return [
        {
            "id": result[0],
            "dataset_url": result[1],
            "dataset_name": result[2],
            "created_by": result[3],
            "created_date": result[4],
            "deleted_by": result[5],
            "deleted_date": result[6],
        } for result in results
    ]

def getAvailable():
  # Returning all available (not booked) tasks
  query = """
          SELECT id, dataset_name
          FROM task 
          EXCEPT 
          SELECT t.id, t.dataset_name
          FROM task t 
          JOIN booking b
          ON t.id = b.task_id
          WHERE b.revoked_date iS NULL
          """
  results = execute_get(query, ())
  return [
    {
      "id": result[0],
      "dataset_name": result[1]
    } for result in results
  ]

def create(dataset_url, dataset_name, created_by):
    query = """
          INSERT INTO task (id, dataset_url, dataset_name,  created_by, created_date)
          VALUES (%s, %s, %s, %s, %s) RETURNING id
          """
    id = generate_id()
    created_date = get_current_time()
    return execute_post(query, (id, dataset_url, dataset_name, created_by, created_date))


def delete(id, deleted_by):
    query = """
            UPDATE task 
            SET 
            deleted_by = %s,
            deleted_date = %s
            WHERE id = %s RETURNING id
            """
    deleted_date = get_current_time()
    return execute_post(query, (deleted_by, deleted_date, id))


BASE = """
SELECT id, dataset_url, dataset_name, created_by, created_date, deleted_by, deleted_date
FROM task 
"""

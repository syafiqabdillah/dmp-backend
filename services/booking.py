from utils.executor import execute_get, execute_post
from utils.auth import get_current_time, generate_id
from fastapi import HTTPException


def create(task_id, created_by):
    try:
        # make booking
        booking_id = generate_id()
        created_date = get_current_time()
        query = """
            INSERT INTO booking (id, task_id, created_by, created_date)
            VALUES (%s, %s, %s, %s) RETURNING id
            """
        return execute_post(query, (booking_id, task_id, created_by, created_date))
    except Exception as e:
        print(e)
        raise HTTPException(500)


def getByUser(username):
    query = """
          SELECT 
          b.id,
          t.dataset_name, 
          t.dataset_url,
          b.created_date
          FROM task t 
          JOIN booking b
          ON t.id = b.task_id
          WHERE b.created_by = %s
          AND b.revoked_date IS NULL
          AND t.deleted_date IS NULL
          ORDER BY b.created_date DESC
          """
    results = execute_get(query, (username, ))
    return [
        {
            "id": result[0],
            "dataset_name": result[1],
            "dataset_url": result[2],
            "booking_date": result[3]
        } for result in results
    ]


def revoke(booking_id):
    query = """
            UPDATE booking
            SET revoked_date = %s
            WHERE id = %s RETURNING id
            """
    revoked_date = get_current_time()
    return execute_post(query, (revoked_date, booking_id))

def getAll():
    query = """
            SELECT id 
            FROM booking
            """
    results = execute_get(query, ())
    return [
        {
            "id": result[0]
        } for result in results
    ]
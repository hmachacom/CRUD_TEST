from core.database import execute_query

def insert_hiring_order(data):
    query = """
        INSERT INTO hiring_order (client, position, exams)
        VALUES (%s, %s, %s)
        RETURNING id;
    """
    params = (data.client, data.position, data.exams)
    return execute_query(query, params, fetch=True)

def get_all_hiring_orders():
    query = "SELECT * FROM hiring_order ORDER BY id;"
    return execute_query(query, fetch=True)

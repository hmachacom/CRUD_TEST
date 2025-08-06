from core.database import execute_query

def insert_job_offer(data):
    query = """
        INSERT INTO job_offer (client, position, city, description)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """
    params = (data.client, data.position, data.city, data.description)
    return execute_query(query, params, fetch=True)

def get_all_job_offers():
    query = "SELECT * FROM job_offer ORDER BY id;"
    return execute_query(query, fetch=True)

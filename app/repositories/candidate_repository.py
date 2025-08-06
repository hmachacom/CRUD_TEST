from core.database import execute_query


def insert_candidate(data):
    query = """
        INSERT INTO candidate (
            first_name, last_name, document_type, document_number, date_of_birth,
            rh, shipping_city, birth_city, home_city
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """
    params = (
        data.first_name, data.last_name, data.document_type, data.document_number,
        data.date_of_birth, data.rh, data.shipping_city, data.birth_city, data.home_city
    )
    return execute_query(query, params, fetch=True)


def get_all_candidates():
    query = "SELECT * FROM candidate ORDER BY id;"
    return execute_query(query, fetch=True)


def deactivate_candidate(candidate_id: int):
    query = "UPDATE candidate SET is_active = FALSE WHERE id = %s;"
    execute_query(query, (candidate_id,))


def get_candidate_by_id(candidate_id: int):
    query = "SELECT * FROM candidate WHERE id = %s;"
    return execute_query(query, (candidate_id,), fetch=True)


def update_candidate(candidate_id: int, data):
    query = """
        UPDATE candidate SET
            first_name = %s, last_name = %s, document_type = %s, document_number = %s,
            date_of_birth = %s, rh = %s, shipping_city = %s, birth_city = %s, home_city = %s
        WHERE id = %s
        RETURNING id;
    """
    params = (
        data.first_name, data.last_name, data.document_type, data.document_number,
        data.date_of_birth, data.rh, data.shipping_city, data.birth_city, data.home_city,
        candidate_id
    )
    return execute_query(query, params, fetch=True)

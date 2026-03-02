from config.db_config import get_connection
from utils.logger import log_info, log_error

def create_user(name, email):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.execute(query, (name, email))
        conn.commit()
        log_info(f"User created: {email}")
        print("User created successfully.")
    except Exception as e:
        conn.rollback()
        log_error(str(e))
        print("Error creating user:", e)
    finally:
        cursor.close()
        conn.close()


def get_all_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()
    return users
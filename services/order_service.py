from config.db_config import get_connection
from utils.logger import log_info, log_error

def create_order(user_id, total_amount):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        conn.start_transaction()

        query = """
        INSERT INTO orders (user_id, order_date, total_amount)
        VALUES (%s, CURDATE(), %s)
        """
        cursor.execute(query, (user_id, total_amount))

        conn.commit()
        log_info(f"Order created for user {user_id}")
        print("Order created successfully.")
    except Exception as e:
        conn.rollback()
        log_error(str(e))
        print("Transaction failed:", e)
    finally:
        cursor.close()
        conn.close()
# services/report_service.py

from config.db_config import get_connection

def generate_sales_report():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        o.order_id,
        u.name AS user_name,
        COALESCE(o.total_amount, 0) AS total_amount
    FROM orders o
    JOIN users u ON o.user_id = u.user_id
    ORDER BY o.order_id DESC
    """

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result
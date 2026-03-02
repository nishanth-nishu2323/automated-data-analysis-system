import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nishu@2328",
    database="automated_analysis"
)
cursor = conn.cursor()


def get_table_columns(table):
    cursor.execute(f"SHOW COLUMNS FROM {table}")
    return [row[0] for row in cursor.fetchall()]


def load_csv(file, table):
    try:
        df = pd.read_csv(file)

        # normalize headers
        df.columns = df.columns.str.strip().str.lower()

        # 🔹 table-specific renaming
        if table == "products":
            df.rename(columns={"name": "product_name"}, inplace=True)

        if table == "orders":
            df.rename(columns={"product_id": "productid"}, inplace=True)

        db_cols = get_table_columns(table)

        # remove auto increment id
        if "id" in db_cols and "id" in df.columns:
            df = df.drop(columns=["id"])

        # keep only matching columns
        df = df[[col for col in df.columns if col in db_cols]]

        cols = ",".join(df.columns)
        vals = ",".join(["%s"] * len(df.columns))
        sql = f"INSERT IGNORE INTO {table} ({cols}) VALUES ({vals})"

        for row in df.itertuples(index=False):
            cursor.execute(sql, tuple(row))

        conn.commit()
        print(f"✅ {table} loaded ({len(df)} rows)")

    except Exception as e:
        print(f"❌ Error loading {table}: {e}")


# 🚀 Load all tables
load_csv("data/users.csv", "users")
load_csv("data/products.csv", "products")
load_csv("data/orders.csv", "orders")

cursor.close()
conn.close()
print("🎉 All data imported successfully!")
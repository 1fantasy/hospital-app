import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="hospital_db",
        user="postgres",
        password="adrielandme2007",
        port="5432"
    )
    print("✅ Connected successfully!")
except Exception as e:
    print("❌ Connection failed:", e)
finally:
    if 'conn' in locals():
        conn.close()

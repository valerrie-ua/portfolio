from datetime import datetime


# =============================
# Модуль 4: Работа с логами
# =============================

def log_query(cursor, conn, query_text):
    insert = "INSERT INTO query_log (query_text, timestamp) VALUES (%s, %s)"
    cursor.execute(insert, (query_text, datetime.now()))
    conn.commit()

def get_popular_queries(cursor):
    query = """
    SELECT query_text, COUNT(*) as count 
    FROM query_log 
    GROUP BY query_text 
    ORDER BY count DESC 
    LIMIT 10
    """
    cursor.execute(query)
    return cursor.fetchall()
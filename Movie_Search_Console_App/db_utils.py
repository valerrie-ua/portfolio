import pymysql


# =============================
# Модуль 2: Подключение к БД
# =============================

def connect_db(host, user, password, dbname):
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=dbname,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except Exception:
        return None


# =============================
# Модуль 3: Поисковые сценарии
# =============================

def search_by_keyword(cursor, keyword):
    keyword_lower = keyword.lower()
    query = """
    SELECT f.title, f.release_year as year, c.name AS genre
    FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    WHERE LOWER(f.title) = %s
       OR LOWER(f.title) LIKE %s
       OR LOWER(f.title) LIKE %s
       OR LOWER(f.title) LIKE %s
    LIMIT 1000
    """
    kw_eq = keyword_lower
    kw_start = keyword_lower + ' %'
    kw_middle = '% ' + keyword_lower + ' %'
    kw_end = '% ' + keyword_lower
    
    cursor.execute(query, (kw_eq, kw_start, kw_middle, kw_end))
    return cursor.fetchall()



def search_by_genre_year(cursor, genre, year):
    query = """
        SELECT f.title, f.release_year as year, c.name AS genre
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        WHERE c.name = %s AND f.release_year = %s
        LIMIT 1000
    """
    cursor.execute(query, (genre, year))
    return cursor.fetchall()


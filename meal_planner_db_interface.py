import psycopg2
from config import load_config

def insert_item(name, price):
    sql = """INSERT INTO items(name, price)
             VALUES(%s, %s) RETURNING item_id;"""
    item_id = None
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (name,price))
                rows = cur.fetchone()
                if rows:
                    item_id = rows[0]
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return item_id
    
def get_items():
    config  = load_config()
    result = None
    try:
        # TODO: dont open new connection every time running a query
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM items ORDER BY item_id")
                result = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return result
    
def select_item_by_id(item_id):
    config  = load_config()
    sql = """SELECT * FROM items WHERE item_id=(%s);"""   
    result = None
    # TODO: figure out why it cant build queries where id is double digits
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (item_id))
                print("The number of parts: ", cur.rowcount)
                print("cur: " + cur)
                result = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print(result)
        return result
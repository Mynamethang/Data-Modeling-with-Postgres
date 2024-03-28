import psycopg2
from sql_queries import create_table_queries, drop_table_queries
def create_database():
    # connect to postgresSQL
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=12345678")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    # #create sparkifydb DATABASE
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING utf8 TEMPLATE template0")
    
    conn.close()

    conn = psycopg2.connect("host=localhost dbname=sparkifydb user=postgres password=12345678")
    cur = conn.cursor()

    return cur, conn


def drop_table(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_table(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    cur, conn = create_database()

    drop_table(cur, conn)
    print("drop table succesfully!")

    create_table(cur, conn)
    print("create table succesfully!")

    conn.close()

if __name__ == "__main__":
    main()
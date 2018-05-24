import psycopg2
import pprint


def main():
    conn_string = "host='localhost' port=54325 dbname='guest' user='guest' password='guest'"
    print "Connecting to database\n	->%s" % (conn_string)

    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    limit = 10
    cursor.execute("SELECT * FROM actor LIMIT %s", (limit,))

    records = cursor.fetchall()
    pprint.pprint(records)


if __name__ == "__main__":
    main()
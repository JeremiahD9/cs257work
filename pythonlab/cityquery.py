import psycopg2

def isNorthfield():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="dawsonj2",
        user="dawsonj2",
        password="eyebrow529redm")

    cur = conn.cursor()

    query = "SELECT city_name FROM cities WHERE city_name = 'Northfield'"

    cur.execute(query)
    row = cur.fetchall()

    if row == None:
        row = "Northfield could not be found in the database"
    
    return row

def main():
    print(isNorthfield())

main()




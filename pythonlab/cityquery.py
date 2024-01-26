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

    if row == "":
        row = "Northfield could not be found in the database"
    
    print(row)
    
    return None

def main():
    isNorthfield()

main()




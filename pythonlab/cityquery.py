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

    if len(row) == 0:
        row = "Northfield could not be found in the database"
    
    print(row)
    
    return None

def largestPopulation():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="dawsonj2",
        user="dawsonj2",
        password="eyebrow529redm")

    cur = conn.cursor()

    query = "SELECT city_population FROM cities"
    cur.execute(query)
    row_list = cur.fetchall()
    largestPop = 0

    for row in row_list:
        print(row[0])
        if(row[0] > int(largestPop)):
            largestPop = row[0]
    
    query = "SELECT city_population FROM cities WHERE city_population = %s"
    cur.execute(query, [largestPop])
    row_list = cur.fetchall()
    
    print(row_list)
    
    return None

def main():
    isNorthfield()
    largestPopulation()

main()




import psycopg2
import sys

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
        if(row[0] > int(largestPop)):
            largestPop = row[0]
    
    query = "SELECT city_name, city_population FROM cities WHERE city_population = %s"
    cur.execute(query, [largestPop])
    row_list = cur.fetchall()
    
    print("City Name: ", row_list[0][0], ", City Population: ", row_list[0][1])
    
    return None

def smallestPopulationMN():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="dawsonj2",
        user="dawsonj2",
        password="eyebrow529redm")

    cur = conn.cursor()

    query = "SELECT city_population FROM cities WHERE city_name = 'Minnesota'"
    cur.execute(query)

    row_list = cur.fetchall()
    smallestPop = sys.maxsize

    for row in row_list:
        if(row[0] < smallestPop):
            smallestPop = row[0]

    query = "SELECT city_name, city_population FROM cities WHERE city_population = %s"

    cur.execute(query, [smallestPop])
    row_list = cur.fetchall()

    print("City Name: ", row_list[0][0], ", City Population: ", row_list[0][1])




def main():
    isNorthfield()
    largestPopulation()
    smallestPopulationMN()

main()




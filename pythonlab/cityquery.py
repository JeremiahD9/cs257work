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

    query = "SELECT city_name, city_lat, city_lon FROM cities WHERE city_name = 'Northfield'"

    cur.execute(query)
    row = cur.fetchall()
    
    if len(row) == 0:
        print("Northfield could not be found in the database")
    else:
        print("Northfield (", row[0][1], ", ", row[0][2], ")")

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

    query = "SELECT city_population FROM cities WHERE city_state = 'Minnesota'"
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

def furthestDir():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="dawsonj2",
    user="dawsonj2",
    password="eyebrow529redm")
    
    cur = conn.cursor()

    query = "SELECT city_lat, city_lon, city_name FROM cities"
    cur.execute(query)
    row_list = cur.fetchall()

    furthestNorth = sys.float_info.min
    furthestSouth = sys.float_info.max
    furthestEast = -500
    furthestWest = sys.float_info.max

    northCity = ""
    southCity = ""
    eastCity = ""
    westCity = ""
    
    # row[0] is lat (North & South) and row[1] is long (East & West)
    for row in row_list:
        if row[0] > furthestNorth:
            furthestNorth = row[0]
            northCity = row[2]
        if(row[0] < furthestSouth):
            furthestSouth = row[0]
            southCity = row[2]
        if(row[1] > furthestEast):
            furthestEast = row[1]
            eastCity = row[2]
        if(row[1] < furthestWest):
            furthestWest = row[1]
            westCity = row[2]
    
    query = "SELECT city_name, city_lat, city_lon FROM cities WHERE city_name = %s"
    cur.execute(query, [northCity])
    northRow = cur.fetchall()

    query = "SELECT city_name, city_lat, city_lon FROM cities WHERE city_name = %s"
    cur.execute(query, [southCity])
    southRow = cur.fetchall()

    
    query = "SELECT city_name, city_lat, city_lon FROM cities WHERE city_name = %s"
    cur.execute(query, [eastCity])
    eastRow = cur.fetchall()
    #print("City Name 2.0: ", eastRow[0][0])
    

    query = "SELECT city_name, city_lat, city_lon FROM cities WHERE city_name = %s"
    cur.execute(query, [westCity])
    westRow = cur.fetchall()

    print(" Furthest City North: ", northRow[0][0], " (", northRow[0][1], ", ", northRow[0][2], ")\n",
         "Furthest City South: ", southRow[0][0], " (", southRow[0][1], ", ", southRow[0][2], ")\n",
         "Furthest City East: ", eastRow[0][0], " (", eastRow[0][1], ", ", eastRow[0][2], ")\n",
         "Furthest City West: ", westRow[0][0], " (", westRow[0][1], ", ", westRow[0][2], ")")

    


def findPopulation():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="dawsonj2",
        user="dawsonj2",
        password="eyebrow529redm")

    cur = conn.cursor()
    user = input("Enter State: ")


    
    query = "SELECT city_name, city_population FROM cities WHERE city_state = %s"
    query2 = "SELECT state_name FROM states WHERE state_abb = %s"
    
    cur.execute(query2, [user])
    row2_list = cur.fetchall()
    
    if len(row2_list) == 0:
        cur.execute(query, [user])
        row_list = cur.fetchall()
        for row in row_list:
            print("City:", row[0], ", Population:", row[1])
    else:
        cur.execute(query, [row2_list[0][0]])
        row_list = cur.fetchall()
        for row in row_list:
            print("City:", row[0], ", Population:", row[1])

    


    








def main():
    isNorthfield()
    largestPopulation()
    smallestPopulationMN()
    furthestDir()
    findPopulation()

main()




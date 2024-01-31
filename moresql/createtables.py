import psycopg2



def create_tables():
    """ create tables in the PostgreSQL database"""
    

    command1 = """CREATE TABLE CityPopulation (
            state_abb VARCHAR(255) NOT NULL,
            state_name VARCHAR(255) NOT NULL,
            state_pop INTEGER NOT NULL
        )"""
        
    
    
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="dawsonj2",
            user="dawsonj2",
            password="eyebrow529redm")
        cur = conn.cursor()
        # create table one by one
        cur.execute(command1)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



    
# This function tests to make sure that you can connect to the database
def test_connection():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="dawsonj2",
        user="dawsonj2",
        password="eyebrow529redm")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    return None

def main():
  test_connection()
  create_tables()

main()

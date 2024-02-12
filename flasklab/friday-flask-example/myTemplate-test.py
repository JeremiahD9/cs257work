from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("SentenceGenerator.html")

@app.route('/rand/<low>/<high>')
def rand(low, high):
    #Input values that come from a URL (i.e., @app.route)
    #   are always strings so I need to convert the type to int
    low_int = int(low)
    high_int = int(high)
    
    num = random.randint(low_int, high_int)
    return render_template("random.html", randNum = num)

@app.route('/sentence')
def randSentence():
    names = ["Jeremiah", "Mason", "Kyle", "SJ", "Josh", "Ma'ki", "Noa", "Noah", "Raghav", "Gus", "Mariana", "Alice", "Mary", "Shanti", "Ahana", "Kiana", "Katelyn", "Monica", "Anthony"]
    adjectives = ["ugly", "cute", "sexy", "weird", "cool", "hot", "creepy", "musty"]
    years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006]

    name = random.choice(names)
    adjective = random.choice(adjectives)
    year = random.choice(years)

    sentence = name + " the " + adjective + " was born in " + randCity() + " in " + str(year)
    return render_template("SentenceGenerator.html", randomSentence = sentence)


def randCity():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="dawsonj2",
        user="dawsonj2",
        password="eyebrow529redm")

    cur = conn.cursor()
    query = "SELECT * FROM cities ORDER BY RANDOM()"
    cur.execute(query)

    row_list = cur.fetchall()

    return row_list[0][0]


if __name__ == '__main__':
    my_port = 5124
    app.run(host='0.0.0.0', port = my_port) 

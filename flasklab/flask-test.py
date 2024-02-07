import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Noah got small PP"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def addition(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    addNum = num1 + num2
    the_string = str(num1) + "+" + str(num2) + "=" + str(addNum)
    return the_string

@app.route('/pop/<ab>')
def findPop(ab):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="dawsonj2",
        user="dawsonj2",
        password="eyebrow529redm")

    cur = conn.cursor()
    
    query = "SELECT state_pop FROM CityPopulation WHERE state_abb = %s"
    
    cur.execute(query, [ab])
    row_list = cur.fetchall()
    
    for row in row_list:
        statePop += row[0]

    return str(statePop)
    

if __name__ == '__main__':
    my_port = 5124
    app.run(host='0.0.0.0', port = my_port) 


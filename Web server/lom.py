from flask import Flask, render_template, jsonify, request
import psycopg2
import json
import time

app = Flask("dom")

table3=[]
conn=psycopg2.connect(host='localhost',database='inventory',user='inventory',password='inventory')
cur=conn.cursor()

def update():
    global table3
    cur.execute("select inventory.id,products.name,x,y from inventory "+
                "join products on product_id=products.id "+
                "join shops on shops.id=shop_id "+
                "where shops.name='Generic store';")
    table1=list(cur.fetchall())
    print(table1)
    table2=[]

    cur.execute('select max(x) from inventory')
    maxcoords=[cur.fetchall()[0][0]]

    cur.execute('select max(y) from inventory')
    maxcoords.append(cur.fetchall()[0][0])
    print(maxcoords)
    
    for i in range(0,maxcoords[0]):
        table2.append([])
        for i2 in range(0,maxcoords[1]):
            table2[i].append([])
    
    for i in range(0,len(table1)):
        table2[table1[i][2]-1][table1[i][3]-1].append(table1[i][1])
    
    print(table2)
    table3=[]

    for i in range(0,len(table2)):
        table3.append([])
        for i2 in range(0,len(table2[i])):
            table3[i].append([table2[i][i2]])
            if len(table2[i][i2])==0:
                table3[i][i2].append(2)
            else:
                table3[i][i2].append(0)
            table3[i][i2].append(False)
        
    print(table3)
    time.sleep(5)
    
    
update()
        
@app.route("/")
def hello_world():
    return render_template('something.html')

@app.route('/api')
def api():
    return jsonify(table3)

@app.route("/hello")
def hello_objects():
    return "<p>Hello, objects!</p>"
  
app.run()
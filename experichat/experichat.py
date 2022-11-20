
import psycopg2
from flask import Flask, render_template, jsonify, request
import json

app=Flask("dom")

conn=psycopg2.connect(host='localhost',database='experichat',user='experichat',password='experichat')
cur=conn.cursor()
cur.execute('select * from experichat;')
tably=list(cur.fetchall())
print(tably)


@app.route("/")
def presentable():
    return render_template('experichat.html')
#    return "<script>text=array("+str(tably)+")</script>"+render_template('something.html')

@app.route('/api')
def api():
    return jsonify(tably)

@app.route('/postman', methods = ['POST'])
def postman():
    global tably
    global cur
    pat=request.get_json()
    tably.append(pat)
    cat="INSERT INTO experichat (Username, MainText) VALUES ('"+str(pat[0])+"','"+str(pat[1])+"');"
    cur.execute(cat)
    return jsonify(['hello'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

#    app.run(host='127.0.0.1', port=8080)

#cur.execute("""insert into experichat (username,MainText) values ('much me','much testing');""")
#print(conn)
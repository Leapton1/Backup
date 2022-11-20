import psycopg2
from flask import Flask, render_template, jsonify, request
import json
from hashlib import sha256

print(sha256('password'.encode('utf-8')).hexdigest())

app=Flask("dom")

conn=psycopg2.connect(host='localhost',database='security',user='security',password='security')
cur=conn.cursor()
cur.execute('select * from security;')
details=list(cur.fetchall())
print(details)

print(sha256((sha256('password'.encode('utf-8')).hexdigest()+details[0][3]).encode('utf-8')).hexdigest())

@app.route("/")
def presentable():
    return render_template('security.html')

@app.route('/postman', methods = ['POST'])
def postman():
    global details
    pat=request.get_json()
    if details[0][1]==pat[0] and details[0][2]==sha256((sha256(pat[1].encode('utf-8')).hexdigest()+details[0][3]).encode('utf-8')).hexdigest():
        return jsonify([True])
    else:
        return jsonify([False])
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, ssl_context=('cert.pem', 'key.pem'))
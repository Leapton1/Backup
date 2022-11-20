from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('serversound.html')


app.run(host='127.0.0.1', port=8080)
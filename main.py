from flask import Flask, request, render_template, url_for
from database.db_management import pullTop20FromDatabase,push1ToDatabase

app = Flask(__name__)

@app.route("/leaderboard_push1",methods=['POST'])
def leaderboard_push1():
    push1ToDatabase("player1",100)
    return "<h1>CONNECTION SUCCESSFUL</h1>"

@app.route("/leaderboard_pull20",methods=['GET'])
def leaderboard_pull20():
    return pullTop20FromDatabase()

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',ssl_context=('../cert.pem', '../key.pem'))

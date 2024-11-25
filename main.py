from flask import Flask, request, render_template, jsonify, make_response
from flask_cors import CORS, cross_origin
from http import HTTPStatus
from database.db_management import pullTop20FromDatabase,push1ToDatabase

app = Flask(__name__)
CORS(app)

@app.route("/leaderboard_push1",methods=['POST'])
def leaderboard_push1():
    data = request.get_json()
    player_name = data.get('user')
    player_score = data.get('score')

    push1ToDatabase(player_name,player_score)

    response = make_response(jsonify(
        {
            "player_score": player_score,
            'player_name': player_name,
            "HTTP Status" : HTTPStatus.OK.value}), HTTPStatus.OK.value)  
    
    return response

@app.route("/leaderboard_pull20",methods=['GET'])
def leaderboard_pull20():
    item_list = pullTop20FromDatabase()

    response = make_response(item_list, HTTPStatus.OK.value)  

    return response

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',ssl_context=('../cert.pem', '../key.pem'))

from flask import Flask, request, render_template, url_for
from database.db_config import DB_HOST,DB_NAME,DB_USER,DB_PASS
import pymysql.cursors

def create_connection():
        connection = pymysql.connect(host=DB_HOST,
                                        user=DB_USER,
                                        password=DB_PASS,
                                        database=DB_NAME,
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor)
        return connection

def pullTop20FromDatabase():
    con = create_connection()
    res = ""
    with con:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM leaderboard ORDER BY score DESC LIMIT 20")
            res = cursor.fetchall()

    return res

def push1ToDatabase(player_name:str,player_score:int) -> str:
    con = create_connection()
    with con:
        with con.cursor() as cursor:
            sql = "INSERT INTO `leaderboard` (`user`, `score`) VALUES (%s, %s)"
            cursor.execute(sql,(player_name,str(player_score)))

        con.commit()

    return "Insertion Successful"
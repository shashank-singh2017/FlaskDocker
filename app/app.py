from typing import List, Dict
from flask import Flask
from flask import request
import mysql.connector
import json
import re

app = Flask(__name__)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'netskope'
}

def wordmap() -> List[Dict]:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM wordcount')
    results = [{word: count} for (word, count) in cursor]
    cursor.close()
    connection.close()
    return results

def insert_word(dict):
    # convert dict to a list of tuples
    records = dict.items()

    query = "INSERT INTO wordcount(word,count) " \
            "VALUES(%s,%s)"

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(prepared=True)

    result  = cursor.executemany(query, records)

    connection.commit()

    cursor.close()
    connection.close()

def countWordFreq(queryWord):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = "SELECT * FROM wordcount where word = %s"
    cursor.execute(query, (queryWord,))
    results = [{word: count} for (word, count) in cursor]
    cursor.close()
    connection.close()
    return results

def countWordWithPattern(pattern):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = "SELECT * FROM wordcount where INSTR(word, %s)"
    cursor.execute(query, (pattern,))
    results = [{word: count} for (word, count) in cursor]
    cursor.close()
    connection.close()
    return results

@app.route('/wordscount')
def hello() -> str:
    return json.dumps({'wordcount': wordmap()})

@app.route('/wordcount/<word>')
def wordcount(word):
    return json.dumps({'wordcount': countWordFreq(word)})

@app.route('/matchword/<pattern>')
def wordWithPattern(pattern):
    return json.dumps({'wordcount': countWordWithPattern(pattern)})

@app.route('/import')
def importFile():
    my_file_handle=open("harrypotter", "r")
    text = my_file_handle.read()

    text = text.strip()
    wordArr = re.split("\s+", text)

    thisdict = {}

    for word in wordArr:
        if word == '':
            continue

        word = re.sub('^(\W)*', "", word)

        word = re.sub('(\W)*$', "", word)

        if word in thisdict:
            count = thisdict[word]
            thisdict[word] = count+1
        else:
            thisdict[word] = 1

    # inserting the data to check insrt happening or not.
    insert_word(thisdict)

    return "some opeartion going on"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

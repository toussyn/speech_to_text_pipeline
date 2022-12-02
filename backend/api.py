from flask import *
from kafka import KafkaAdminClient
from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads, dumps
import random 
import pandas as pd
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
from datetime import datetime
# import logging
import sqlite3

# logging.basicConfig(filename='../log/log.log', filemode='a',encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "/mnt/10ac-batch-6/notebooks/natnael_melese/data/"
# app.config["UPLOAD_FOLDER"] = "/home/natnael_melese/audio_data"
CORS(app)

@app.route('/get_text', methods=['GET'])
def get_text():
    
    try:
        if request.method == "GET": 
            print("#####GETTING TEXT#####")
            data = pd.read_csv('/mnt/10ac-batch-6/notebooks/gedion_abebe/Amharic News Dataset.csv')
            random_text = data.sample(n=1)[["headline","category","article"]]
            random_text.reset_index(drop=True, inplace=True)
            topic_names = {
                "ሀገር አቀፍ ዜና": "g2-national_news",
                "መዝናኛ": "g2-entertainment",
                "ቢዝነስ": "g2-business",
                "ዓለም አቀፍ ዜና": "g2-international_news",
                "ፖለቲካ":"g2-politics",
                "ስፖርት":"g2-sport"
            }

            return jsonify({
                "status": "success",
                "topic": topic_names[random_text['category'][0]],
                "headline": random_text['headline'][0].strip(),
                "category": random_text['category'][0].strip(),
                "article":random_text['article'][0].strip()
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"{request.method} is not allowed"
            })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

@app.route('/get_audio', methods=['POST'])
def get_audio():
    try:
        if request.method == "POST":
            producer = KafkaProducer(
                        bootstrap_servers=['b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092','b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092'],
                        client_id='g2-text-producer',value_serializer=lambda x: dumps(x).encode('utf-8'))
            headline = request.form.get("headline")
            article = request.form.get("article")
            json_id = request.form.get("json_id")
            audio_file = request.files["file"]
            if audio_file.filename != '':
                filename = secure_filename(audio_file.filename)
                file_path = app.config["UPLOAD_FOLDER"] + filename + f"{datetime.now()}"
                audio_file.save(file_path)
                print(file_path)
                producer.send("g2-audio-raw",{"headline":headline,"article":article,"json_id":json_id,"file_path":file_path}).get(timeout=30)
            return jsonify({"status": "success","file_path":file_path})
        else:
            return{
                "status": "error",
                "message": f"{request.method} is not allowed"
            }
    except Exception as e:
        return{
            "status": "error",
            "message": str(e)
        }

@app.route('/return_processed_audio', methods=['POST'])
def return_processed_audio():
    try:
        if request.method == "POST":
            conn = sqlite3.connect('processed_audio.db')
            # json_id = request.get_json()["json_id"]
            cursor = conn.execute("SELECT json_id, headline, article, file_path from Audio")
            data = []
            for row in cursor:
                json_id = row[0]
                headline = row[1]
                article = row[2]
                file_path = row[3]
                audio_file = open("{}".format(file_path), "rb").read()
                data.append({
                    "json_id":json_id,
                    "headline":headline,
                    "article":article,
                    "audio_file":audio_file
                })
            return jsonify({
                "status": "success",
                "data": data
            })
        else:
            return{
                "status": "error",
                "message": f"{request.method} is not allowed"
            }
    except Exception as e:
        return{
            "status": "error",
            "message": str(e)
        }

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', debug=True, port=port)

    

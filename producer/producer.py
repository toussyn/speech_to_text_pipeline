from flask.views import MethodView
from flask import *
from kafka import KafkaAdminClient 
from kafka.admin import NewTopic

app = Flask(__name__)
class Admin(MethodView):
    init_every_request = False

    def __init__(self):
        self.client = KafkaAdminClient(
            bootstrap_servers = ['b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092','b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092'],
            api_version=(0,11,5),
        )
    
    def get(self):
        api_version = self.client.config['api_version']
        topics_list = self.client.list_topics()
        g2_topics_list = []
        for i in topics_list:
            if 'g2' in i:
                g2_topics_list.append(i)
        return jsonify({
            "success": True,
            "api_version":api_version,
            "created_g2_topics":g2_topics_list
        })
    
    def post(self):
        try:
            print(request.json)
            data = request.json
            topic_name = data.get('topic_name')
            if topic_name:
                return jsonify({ 
                    "success": True,
                    "message": "POST"
                })
            else:
                return jsonify({
                    "success": False,
                    "message": "Topic name required"
                })
        except Exception as e:
            return jsonify({
                "success": False,
                "message": str(e)
            })

test_get = Admin.as_view("admin")
app.add_url_rule("/admin", view_func=test_get)

if __name__ == '__main__':
    app.run()
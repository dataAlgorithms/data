from flask import jsonify
from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/ghr')
def get_current_user():
    edgeip = request.args.get('edgeip')
    clientip = request.args.get('clientip')
    clientdomain = request.args.get('clientdomain')

    str = {"status":["302"], "value":[clientip]}

    return jsonify(str )

if __name__ == '__main__':
    app.run(debug=True,  port=9120)
    
'''
curl -i "http://127.0.0.1:9120/ghr?edgeip=171.107.87.8&clientip=202.106.3.5&clientdomain=pl6.panda.tv"
'''

import os
import json
import requests

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_restful import Resource, Api, request

load_dotenv(find_dotenv())
print(os.getenv('API_KEY'))
API_KEY = os.getenv('API_KEY')

app = Flask(__name__)
api = Api(app)


class Articles(Resource):
    def get(self):
        num = request.args.get('num', 10)
        return json.loads(requests.get(f'https://gnews.io/api/v4/top-headlines?max={num}&token={API_KEY}').text) \
            ['articles']


api.add_resource(Articles, '/articles')


if __name__ == '__main__':
    app.run(debug=True)
    # x = requests.get('https://gnews.io/api/v4/search?q=example&token=' + API_KEY)
    # print(x)

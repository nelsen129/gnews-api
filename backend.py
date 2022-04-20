import os
import json
import requests

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_restful import Resource, Api, request
from flask_caching import Cache

load_dotenv(find_dotenv())
print(os.getenv('API_KEY'))
API_KEY = os.getenv('API_KEY')

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)
api = Api(app)


def cache_key():
    return request.url


class Articles(Resource):
    @cache.cached(timeout=10, key_prefix=cache_key)
    def get(self):
        num = request.args.get('num', 10)
        return json.loads(requests.get(f'https://gnews.io/api/v4/top-headlines?max={num}&token={API_KEY}').text) \
            ['articles']


api.add_resource(Articles, '/articles')


if __name__ == '__main__':
    app.run(debug=True)
    # x = requests.get('https://gnews.io/api/v4/search?q=example&token=' + API_KEY)
    # print(x)

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
        topic = request.args.get('topic', None)
        query = request.args.get('q', None)
        from_date = request.args.get('from', None)
        to_date = request.args.get('to', None)

        req_queries = [
            f'num={num}',
            f'q={query}',
            f'from={from_date}',
            f'to={to_date}'
        ]
        if topic is not None:
            req_queries.append(f'topic={topic}')

        req_queries.append(f'token={API_KEY}')

        request_str = 'https://gnews.io/api/v4/'
        if topic is not None or query is None:
            request_str += 'top-headlines?'
        else:
            request_str += 'search?'
        request_str += '&'.join(req_queries)

        return json.loads(requests.get(request_str).text)['articles']


api.add_resource(Articles, '/articles')


if __name__ == '__main__':
    app.run()

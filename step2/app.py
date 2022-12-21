import flask
from redis import Redis
import requests
import os


app = flask.Flask(__name__)
redis_db = Redis(host='redis', port=6379, db=0)

CACHE_EXPIRE_TIME = int(os.getenv('CACHE_EXPIRE_TIME'))
SERVER_PORT = int(os.getenv('SERVER_PORT'))
COIN_NAME = os.getenv('COIN_NAME')


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


@app.route('/')
def get_coin_price():
    coin_name = COIN_NAME
    price = redis_db.get(coin_name)
    if price is None:
        price = requests.get(
            f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin_name}').json()[0]['current_price']
        redis_db.set(coin_name, price, ex=CACHE_EXPIRE_TIME)
    price_val = redis_db.get(coin_name).decode("utf-8")
    return {"name": coin_name, "price": price_val}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=SERVER_PORT, debug=True)

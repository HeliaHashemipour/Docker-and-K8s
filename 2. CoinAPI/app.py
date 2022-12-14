import requests
import flask
import redis


app = flask.Flask(__name__)
redis_db = redis.Redis(host='redis', port=6379, db=0)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get_coin_price/', methods=['GET'])
def get_coin_price():
    coin = flask.request.args.get('coin')
    price = redis_db.get(coin)
    if price is None:
        price = requests.get(
            'https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd'.format(coin)).json()[coin]['usd']
        redis_db.set(coin, price)

    return price

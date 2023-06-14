from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongodb:27017/')
db = client['food_db']
collection = db['food_collection']


@app.route('/health')
def health_check():
    return "OK"


@app.route('/foods', methods=['GET'])
def get_foods():
    foods = collection.find({}, {'_id': 0})
    return jsonify(foods)


@app.route('/foods', methods=['POST'])
def add_foods():
    foods = request.get_json()
    collection.insert_many(foods)
    return "Foods added to MongoDB"


if __name__ == '__main__':
    app.run(host='0.0.0.0')


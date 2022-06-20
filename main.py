from flask import Flask, jsonify, request
from sqlalchemy import true
from database import delete, get, create

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_growth():
    return get()


@app.route('/store', methods=['POST'])
def add_growth():
    if not request.is_json:
        return jsonify({"message": "JSON not found"}), 400

    create(request.get_json())
    return 'Growth History Added'

@app.route('/gr/<id>', methods=['DELETE'])
def gr_delete(id):
    delete(id)
    return 'growth deleted'
   
    
    


if __name__ == '__main__':
    app.run()
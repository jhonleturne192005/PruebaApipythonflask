from flask import Flask
from flask import jsonify
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/api/saludo', methods=['GET'])
def get_saludo():
    response = {'message': 'hola mundo'}
    return jsonify(response),200

@app.route('/api/products', methods=['GET'])
def get_products():
    list_products=["coca-cola","pepsi","sprite","fanta","manzanita","7up"]
    response = {'products': list_products}
    return jsonify(response),200

@app.route('/api/entorno', methods=['GET'])
def get_environment():
    NAME_API=os.getenv('PROGRAM', 'default_value')
    response = {'environment': NAME_API}
    return jsonify(response),200

@app.route('/api/entornofile', methods=['GET'])
def get_environment():
    NAME_API=os.getenv('NOMBRE_BD', 'default_value')
    response = {'environment': NAME_API}
    return jsonify(response),200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=5000)
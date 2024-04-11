from flask import Flask, jsonify,redirect, request, send_file, url_for
import json
# from django.http import response
from flask import jsonify  # For JSON responses
from blockchain import SupplyChainBlockchain

#intitializing flask
app = Flask(__name__)
blockchain = SupplyChainBlockchain()

# @app.route("/add/user", methods=['POST'])
# def add_user():
    
    

@app.route("/users", methods = ['GET'])
def showUsers():
    users = blockchain.nodes
    response={
        'users':users
    }

    return jsonify(response),200


# @app.route("/add/transaction", methods=['POST'])
# def add_transaction():

# @app.route("/transactions", methods=['GET'])
# def list_transactions():

# @app.route("/mine", methods=['GET'])
# def mine_block():

@app.route("/chain", methods=['GET'])
def get_chain():
    response={
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
    }
    return jsonify(response),200

# @app.route("/register/node", methods=['POST'])
# def register_node():

# @app.route("/resolve", methods=['GET'])
# def resolve_conflicts():

# @app.route("/product/<product_id>", methods=['GET'])
# def view_product_history(product_id):

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help='Listening on port')
    args = parser.parse_args()
    port = args.port
    app.run(host = '0.0.0.0', port = port, debug=True)








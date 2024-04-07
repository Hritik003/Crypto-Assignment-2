from flask import Flask, jsonify,redirect, request, send_file, url_for
import json
from flask import jsonify  # For JSON responses
from blockchain import SupplyChainBlockchain
import uuid
import random

app = Flask(__name__)
blockchain = SupplyChainBlockchain()

@app.route("/add/user", methods=['POST'])
def add_user():
    
    

@app.route("/users")
def showUsers():
    users = SupplyChainBlockchain.users
    response={
        'users':users
    }

    return jsonify(response),200


@app.route("/add/transaction", methods=['POST'])
def add_transaction():

@app.route("/transactions", methods=['GET'])
def list_transactions():

@app.route("/mine", methods=['GET'])
def mine_block():

@app.route("/chain", methods=['GET'])
def get_chain():

@app.route("/register/node", methods=['POST'])
def register_node():

@app.route("/resolve", methods=['GET'])
def resolve_conflicts():

@app.route("/product/<product_id>", methods=['GET'])
def view_product_history(product_id):










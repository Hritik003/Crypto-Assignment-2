from secrets import token_hex
from flask import Flask, jsonify,redirect, request, send_file, url_for
import json

from flask import jsonify  
from blockchain import SupplyChainBlockchain


app = Flask(__name__)
blockchain = SupplyChainBlockchain()
    

@app.route("/users", methods = ['GET'])
def showUsers():
    users = blockchain.nodes
    response={
        'users':users
    }

    return jsonify(response),200

@app.route("/register",methods=['POST'])
def register():
    users = request.json
    new_users = {}
    for user, details in users.items():

        secret_key = token_hex(16) 
        new_users[user] = {**details, 'secret_key': secret_key}

    blockchain.node(new_users)
    response={
        'message':"the following participants have been added",
        'participants':users
    }

    return jsonify(response),200



@app.route("/add/transaction", methods=['POST'])
def list_transactions():
    # client - bob, distributor - alice
    data = request.json
    client = data.get('receiver')
    product = data.get('product')
    distributor = data.get('sender')
  
    amount = data.get('amount', 0)

    if distributor not in blockchain.nodes:
        return jsonify({"error":"Distributor does not exist in this blockchain"})

    dis = blockchain.nodes[distributor]

    
    if  'property' in dis and product in dis['property']:
        blockchain.create_transaction(sender=distributor, receiver=client, product=product,amount=amount)
        return jsonify("transaction added"),200
    else:
        return jsonify("distributor does not own this properties"),201

    

@app.route("/mine", methods=['GET'])
def mine_block():
    block = blockchain.create_block()
    response = {
        'message': 'New Block Mined!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'transactions': block['transactions'],
        'merkle_root': block['merkle_root'],
        'previous_hash': block['previous_hash'],
        'proof': block['proof']
    }

    print("Transactions in the new block:", len(block['transactions']))
    return jsonify(response), 200


@app.route("/chain", methods=['GET'])
def get_chain():
    response={
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
    }
    return jsonify(response),200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001, type=int, help='Listening on port')
    args = parser.parse_args()
    port = args.port
    app.run(host = '0.0.0.0', port = port, debug=True)








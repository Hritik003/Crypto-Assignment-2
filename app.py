from secrets import token_hex
from flask import Flask, jsonify,redirect, request, send_file, url_for
import json

from flask import jsonify  
from blockchain import SupplyChainBlockchain


app = Flask(__name__)
blockchain = SupplyChainBlockchain()
    
@app.route('/view_user/<user_id>', methods=['GET'])
def viewUser(user_id):
    user_transactions = []
    for transaction in blockchain.curr_transactions:
        if transaction['sender'] == user_id or transaction['receiver'] == user_id:
            user_transactions.append(transaction)

    if not user_transactions:
        return jsonify({'message': 'No transactions found for this user.'}), 404

    return jsonify({
        'user_id': user_id,
        'transactions': user_transactions
    }), 200

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

@app.route("/list/transaction",methods=['GET'])
def list_transactions():
    trans = blockchain.curr_transactions
    response={
        'transactions':trans

    }
    return jsonify(response),200

@app.route("/add/transaction", methods=['POST'])

def create_transactions():
    # client - bob, distributor - alice
    data = request.json
    client = data.get('client')
    product = data.get('product')
    distributor = data.get('sender')
  
    amount = data.get('amount', 0)

    if distributor not in blockchain.nodes:
        return jsonify({"error":"Distributor does not exist in this blockchain"})
    if client not in blockchain.nodes:
        return jsonify({"error":"client does not exist in this blockchain"})

    if  'property' in blockchain.nodes[distributor] and product in blockchain.nodes[distributor]['property']:
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








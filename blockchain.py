import hashlib
import hmac
import json
import random
import time  # Add this import statement
import os

from merkletree import MerkleTree

SECRET_KEY = "your_secret_key_here"

class SupplyChainBlockchain:
    def __init__(self):
        self.nonce = random.randint(100,999)
        self.chain=[]
        self.curr_transactions=[]
        self.nodes=dict()
        self.create_genesis_block()
    
    def node(self, nodes):
        self.nodes.update(nodes)
    
    def create_genesis_block(self):
        block = self.create_block(proof=100, previous_hash='1')
        return block
        
    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),  # Use time.time() instead of time()
            'transactions': self.curr_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            'merkle_root': self.generate_merkle_root(self.curr_transactions),
            'nonce':self.nonce
        }
        self.curr_transactions = []
        self.chain.append(block)
        return block


    def generate_merkle_root(self, transactions):
        mt = MerkleTree()
        for tx in transactions:
            tx_string = json.dumps(tx, sort_keys=True)
            tx_hex = tx_string.encode('utf-8').hex()
            mt.add_leaf(tx_hex)
        mt.make_tree()
        return mt.generate_merkle_root()
    

    def create_transaction(self, sender, receiver,product, amount):
        challenge = self.generate_challenge
        print(challenge)
        message = f"{sender}{receiver}{product}{amount}"
        print(message)
        bit = random.randint(0,1)
        print(bit)
        
        secret_key = self.nodes[sender]['secret_key']
        print(secret_key)
        response = self.create_response(message,secret_key, challenge, bit)
        print(response)

        transaction = {
            'sender': sender,
            'receiver': receiver,
            'product':product,
            'amount': amount,
        }

        if not self.verify_response(message, secret_key,challenge, bit, response):
            raise Exception('Invalid transaction')

        self.curr_transactions.append(transaction)
        
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof
        
    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
        
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        
    def last_block(self):
        return self.chain[-1]
        
    def nodes(self, users):
        self.users.update(users)
    
    def verify_response(self, message, secret_key, challenge, bit, response):
        expected_response = self.create_response(message, secret_key, challenge, bit)  
        print(expected_response)
        return response == expected_response  

    def generate_challenge(self):
        return os.urandom(16).hex()  

    def create_response(self,message, secret_key, challenge, bit):

        # secret_key = self.nodes[node_id]['secret_key']
        challenge_bit_combo = f"{message}{challenge}{bit}".encode()
        return hmac.new(secret_key.encode(), challenge_bit_combo, hashlib.sha256).hexdigest()

    
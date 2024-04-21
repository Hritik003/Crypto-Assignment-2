import hashlib
import hmac
import json
import random
import time  # Add this import statement
import os

from merkletree import MerkleTree


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

        self.curr_transactions = []
        self.nonce = random.randint(100, 999)
        block = self.create_block()
        block['proof'] = 100  
        block['previous_hash'] = '1'  
        return block
        
    def create_block(self):
        if self.chain:
            last_block = self.chain[-1]
            previous_hash = self.hash(last_block)
        else:
            previous_hash = '1'

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.curr_transactions,
            'previous_hash': previous_hash,
            'nonce': 0, 
            'merkle_root': self.generate_merkle_root(self.curr_transactions)
        }

        block['nonce'] = self.proof_of_work(block)
        self.curr_transactions = []
        self.chain.append(block)
        return block

    def generate_merkle_root(self, transactions):
        mt = MerkleTree()
        transaction_hashes = [hashlib.sha256(json.dumps(tx, sort_keys=True).encode()).hexdigest() for tx in transactions]
        mt.add_leaf(transaction_hashes, do_hash=False)
        mt.make_tree()
        return mt.generate_merkle_root()
    

    def create_transaction(self, sender, receiver,product, amount):
        challenge = self.generate_challenge
        print("the challenge generated is {challenge}")
        message = f"{sender}{receiver}{product}{amount}"
        print("the message recieved is {message}")
        bit = random.randint(0,1)
        print("the bit from the system {bit}")
        
        secret_key = self.nodes[sender]['secret_key']
        print("the secret key of the user involved in the transaction : {secret_key}")
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
        
    def proof_of_work(self, block):
        block['nonce'] = 0
        while True:
            block_hash = self.hash(block)
            if block_hash.startswith('0000'):
                return block['nonce']
            else:
                block['nonce'] += 1

        
    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
        
    @staticmethod
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

    
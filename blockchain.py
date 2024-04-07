import hashlib
import hmac
import json
import time

from merkletree import MerkleTree

SECRET_KEY = "your_secret_key_here"

class blockchain:
    def __init__(self):
        self.chain=[]
        self.curr_transactios=[]
        self.nodes=dict()

        self.create_genesis_block()
    
    def create_genesis_block(self):
        block = self.create_block(proof=100, previous_hash='1')
        return block
        
    def create_block(self, proof, previous_hash):
        
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            'merkle_root': self.generate_merkle_root(self.current_transactions),
        }

        self.current_transactions = []
        self.chain.append(block)
        return block
    # Generate the Merkle root of transactions

    def generate_merkle_root(self, transactions):
        mt = MerkleTree()
        for tx in transactions:
            tx_string = json.dumps(tx, sort_keys=True)
            tx_hex = tx_string.encode('utf-8').hex()
            mt.add_leaf(tx_hex)
        mt.make_tree()
        return mt.generate_merkle_root()
    

    def create_transaction(self, sender, receiver, amount, signature):

        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'message': f'{sender}{receiver}{amount}', 
            'signature': signature,  
        }

        
        if not self.verify_transaction(transaction, SECRET_KEY):
            raise Exception('Invalid transaction')
        
        self.current_transactions.append(transaction)
        
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
        
    def verify_transaction(self, transaction, secret_key):

        message = transaction.get('message')
        signature = transaction.get('signature')

        hmac_generated = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()
        
        return hmac.compare_digest(hmac_generated, signature)
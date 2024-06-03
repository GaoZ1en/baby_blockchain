#imports the Block class from block.py
from block import Block

class Blockchain:
    def __init__(self):
        # initializing instance variables chain and all_transactions as empty Python lists
        self.chain = []
        self.all_transactions = []
        self.genesis_block()
        pass

    def genesis_block(self):
        # initializing instance variables transactions and previous_hash as required
        transactions = ["Gensis Block"]
        previous_hash = 0

        # instantiating a new Block object and append it to the chain
        genesis_block = Block(transactions, previous_hash)
        self.chain.append(genesis_block)

        #return self.chain
        return self.chain

    # prints contents of blockchain
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()
        pass

    # add block to blockchain `chain`
    def add_block(self, transactions):
        # Create previous_block_hash that stores previous block‘s hash
        previous_hash = self.chain[-1].hash

        # Create new_block that takes in a transaction and the previous_block‘s hash
        new_block = Block(transactions, previous_hash)

        # Calculate the proof of work for the new_block
        proof = self.proof_of_work(new_block)

        # Append new_block to the end of the chain.
        self.chain.append(new_block)

        return proof, new_block

    def validate_chain(self):
        # Create a loop to validate all the blocks except the very first Genesis Block
        for i in range(1, len(self.chain)):

        # inside the loop create the variabel "current" and "previous"
            current = self.chain[i]
            previous = self.chain[i-1]

        # Check if the hashes match, return and print the required information
            if current.previous_hash != previous.hash:
                print("Blockchain invalid at block {}".format(i))
                return False
            print("Blockchain valid")
        return True

    def proof_of_work(self,block, difficulty=2):
         # Creat a local variable proof and assign it the block’s hash
        proof = block.hash

        # Creat a loop to find the required proof
        while not proof.startswith('0'*difficulty):
            block.nonce += 1
            proof = block.hash

        # Set nonce back to 0
        block.nonce = 0

        # Return the proof
        return proof

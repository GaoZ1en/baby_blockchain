from datetime import datetime
from hashlib import sha256

class Block:
  def __init__(self, transactions, previous_hash, nonce = 0):
    pass
    # Copy and paste your code here

    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.timestamp = datetime.now()

    # Checkpoint 4
    self.hash = self.generate_hash()
    pass

  def print_contents(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("nonce:", self.nonce)
    print("current hash:", self.generate_hash())
    pass

  def generate_hash(self):
    # hash the blocks contents
    # Checkpoint 1
    # To combine strings together the following syntax is used: string = sub_string1 + sub_string2 + sub_string3

    block_string = str(self.transactions)+str(self.previous_hash)+str(self.nonce)+str(self.timestamp)

    # Checkpoint 2 & 3

    return sha256(block_string.encode()).hexdigest()

import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next_block = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.timestamp}-{self.data}-{self.previous_hash}".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        timestamp = time.gmtime()
        if not self.head:
            self.head = Block(timestamp, data, None)
        else:
            new_block = Block(timestamp, data, self.head.hash)
            new_block.next_block = self.head
            self.head = new_block

    def print_blocks(self):
        current_block = self.head
        while current_block:
            print("Time:", time.strftime(' %H:%M:%S %Y-%m-%d ', current_block.timestamp))
            print("Data:", current_block.data)
            print("Previous Hash:", current_block.previous_hash)
            print("Hash:", current_block.hash)
            print() 
            current_block = current_block.next_block

blockchain = Blockchain()
blockchain.add_block("Bitcoin")
blockchain.add_block("Ethereum")
blockchain.add_block("Litecoin")
blockchain.add_block("")

blockchain.print_blocks()

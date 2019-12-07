import hashlib

class Block :
    def __init__(self, timestamp , transactions , previousHash = ' '):
            #self.index = index 
            self.timestamp = timestamp 
            self.transactions = transactions 
            self.previousHash = previousHash
            self.my_nonce = 0 
            self.hash = self.calculateHash()
            
    
    def calculateHash(self) :
        hash_Value = hashlib.sha256()
        hash_data =  self.previousHash + str(self.timestamp) + str(self.my_nonce) + str(self.transactions)
        hash_data = hash_data.encode('utf-8')
        hash_Value.update(hash_data)
        return str(hash_Value.hexdigest())
    
    #adding mining 
    def mineBlock(self , difficulty): 
        while self.hash[0:difficulty] != '0'*difficulty:
            self.my_nonce  += 1
            self.hash =  self.calculateHash()
            #print(self.hash)
            #print("Loop "+ str(self.my_nonce) + " done")
        print("Block mined " + self.hash)



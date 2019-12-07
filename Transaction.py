import hashlib
from ecpy.ecdsa      import ECDSA

class Transaction():
    def __init__(self, fromAddress , toAddress, amount):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount 
        
    #function to transfrom transactions object to a string 
    
    def __str__(self):
        return str(self.__dict__)
    
    #calculate hash to be signned 
    
    def calculateHash(self) :
        hash_Value = hashlib.sha256()
        hash_data =  self.fromAddress + self.toAddress + str(self.amount)
        hash_data = hash_data.encode('utf-8')
        hash_Value.update(hash_data)
        return str(hash_Value.hexdigest())
     
    #function to sign transactions 
    
    def signTransaction(self, signingKeyPrivate , signingKeyPublic):
        if(signingKeyPublic != self.fromAddress):
            raise Exception('You cannot sign transactions from other wallets!')   
            
        hashTx = self.calculateHash
        signer = ECDSA()
        sig = signer.sign(hashTx,signingKeyPrivate)
        self.signature = sig
        
    def isValid(self):
        if  self.fromAddress == None :
            return True
        
        if self.signature or len(self.signature) == 0:
            raise Exception('No Signature in this transaction')
        
        
    
     
        

from Block import Block 
from Transaction import Transaction
from datetime import datetime as time

class BlockChain: 
    #constructor of Our Blockchain
    def __init__(self):
        self.chain = [self.createGensisBlock()]
        self.__difficulty = 2
        self.pendingTransactions = []
        self.miningReward = 50
    
    #function to generate genesis block 
    def createGensisBlock(self):
        return  Block("10-5-1997 14:04:49.384440" , "Gensis Block" , "0")
    
    def getLastestBlock(self):
        return self.chain[len(self.chain)-1]
    
    #old mining function to add block 
    # def addBlock(self, Block):
    #     Block.previousHash = self.getLastestBlock().hash
    #     #Block.hash = Block.calculateHash()
    #     Block.mineBlock(self.__difficulty)
    #     self.chain.append(Block)
    
    def minePendingTransactions(self , miningRewardAddress):
        block = Block(str(time.now()),self.pendingTransactions)
        block.mineBlock(self.__difficulty)
        print('Block successfully mined! ')
        self.chain.append(block)
        self.pendingTransactions = [
            Transaction(None, miningRewardAddress,self.miningReward)
        ]
    
    def createTransaction(self , transaction):
        self.pendingTransactions.append(transaction)
        
    def getBalanceOfAddress(self, address):   
        balance = 0 
        for block in self.chain:
            if block.transactions != 'Gensis Block': #to avoid error of genisi block not having toaddress and from address
                for trans in block.transactions:
                    if trans.fromAddress == address:
                        balance -= trans.amount
                    if trans.toAddress == address :
                        balance += trans.amount
                               
        return balance    
            
        
        
    def isChainValid(self):
        for x in range(1 ,len(self.chain) ):
            currentBlock = self.chain[x]
            previousBlock = self.chain[x-1]
            
            if currentBlock.hash != currentBlock.calculateHash():
                return False
            
            if currentBlock.previousHash != previousBlock.hash :
                return False
            
        return True
    
            
        

         
        
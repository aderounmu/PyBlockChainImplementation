from BlockChain import BlockChain
from Block import Block 
from Transaction import Transaction

MyBlockChain = BlockChain()

MyBlockChain.createTransaction(Transaction('address1','address2',100))
MyBlockChain.createTransaction(Transaction('address2','address1',50))

print('Start the miner .....')

MyBlockChain.minePendingTransactions('ade_address')
print('Balance is : ' + str(MyBlockChain.getBalanceOfAddress('ade_address')))

MyBlockChain.minePendingTransactions('ade_address')
print('Balance is : ' + str(MyBlockChain.getBalanceOfAddress('ade_address')))



#print(MyBlockChain.chain)
# for items in MyBlockChain.chain :
#     if items.transactions != 'Gensis Block':
#         print(items.transactions[0].toAddress)
        
# for items in MyBlockChain.chain :
#     if items.transactions != 'Gensis Block':
#         for tran in items.transactions:
#             print(tran.toAddress)
        


# for items in MyBlockChain.chain :
#     print(items.transactions.toAddress)
#     print(items.transactions.fromAddress)



#Video 1-2 


# print("Minning block 1 .....")
# MyBlockChain.addBlock(Block(1 , "11/5/1997" , "What ever block chain"))
# print("Minning block 2 .....")
# MyBlockChain.addBlock(Block(2 , "13/5/1997" , "Block Chain Whatever"))

#what = MyBlockChain.chain
#block_no = 1
#for items in what :
#     print('Minning Block ' + str(block_no) + " ....")
#     print("{")
#     print(items.data)
#     print(items.index)
#     print(items.timestamp)
#     print(items.hash)
#     print(items.previousHash)
#     print("}")
#     block_no += 1


# MyBlockChain.chain[1].data = "This is a lie"
# MyBlockChain.chain[1].hash = MyBlockChain.chain[1].calculateHash()
#print(MyBlockChain.isChainValid())





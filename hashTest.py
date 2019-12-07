import hashlib

def calculateHash(stuff , my_nonce) :
        hash_Value = hashlib.sha256()
        #hash_data = self.index + self.previousHash + self.timestamp + self.data
        stuff = stuff + str(my_nonce)
        stuff = stuff.encode('utf-8')
        hash_Value.update(stuff)
        print(hash_Value.hexdigest())
        return hash_Value.hexdigest()
        
myhash = str(calculateHash("23456  588r99rhf  dhdhhdhcbbcjdj  uurur" ,20))
whatever = 0
difficulty = 1
while myhash[0:difficulty] != '0'*difficulty:
    if myhash[0:difficulty] != '0'*difficulty:
        print(False)
    else:
        print(True)
    whatever += 1
    print(whatever)
    myhash = calculateHash("23456  588r99rhf  dhdhhdhcbbcjdj  uurur" ,whatever)
    pass

# if myhash[0:difficulty] != [0]*difficulty:
#     print(False)
# else:
#     print(True)

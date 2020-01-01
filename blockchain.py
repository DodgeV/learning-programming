import hashlib
import datetime as date
class Block:
    def __init__(self,index,timestamp,data,previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    def hash_block(self):
        sha = hashlib.sha256()
        sha.update((str(self.index)+str(self.timestamp)+
                   str(self.data)+str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

def create_genesis_block():
    return Block(0,date.datetime.now(),'Genesis Block','0')
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = 'hey! I\'m block'+str(this_index)
    this_hash = last_block.hash
    return Block(this_index,this_timestamp,this_data,this_hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]
num_of_blocks_to_add = int(input('how many blocks do you wanna add:'))
for i in range(0,num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print('Block {} has been added to the blockchain!'.format(block_to_add.index))
    print('Hash:{}\n'.format(block_to_add.hash))

input('请输入任意键退出:')
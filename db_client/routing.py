from serialize import serialize
from hashing256 import Hashing256
from hashTable import HashTable
import json


class routingTier:

    def __init__(self, partitions):
        self.hash_table = HashTable(partitions)
        self.hash256 = Hashing256()
        self.serilize = serialize(self.hash256)

    def test(self, key):
        return self.hash256.encrypt(key)
      
    def create_key_value(self, key, value):
      return
    

    def find_by_key(self, key):
        key_object = eval(self.hash256.decrypt(key))
        #node_port = self.hash_table.get(key_object.node)
        #partition_number = key_object.partition
        #key_value = key_object.partition

        print(key_object)
        
    def update_by_key(self, key, value):
      return
    
    def delete_by_key(self, key, value):
      return 
      


router = routingTier(50)
dict = {"node": 1231, "partition": 1, "key": 2}
test = router.test(json.dumps(dict))
print(test)
router.findFile(test)

""" router.findFile(test) """

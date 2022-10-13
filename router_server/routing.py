from cryptography.fernet import Fernet
from .hashTable import HashTable
from dotenv import load_dotenv
import requests

load_dotenv()

class routingTier:

    def __init__(self):
        self.current_partition = 1
        key = Fernet.generate_key()
        self.fernet = Fernet(key)

    def replication(self, key, value):
        partition_replication_number = self.current_partition + 1 
        partition_name = "partition%s" % (partition_replication_number, 1)[partition_replication_number > self.partition_number]
        api_url = "%s/create" % self.hash_table.get(partition_name)
        response = requests.post(api_url, json={"key": key, "value": value})
        return (False, True)[response.json() != None]

    def create_key_value(self, key, value):
        try:
            partition = "partition%s" % self.current_partition 
            key_name = partition + ":" + key
            key_hash = self.encrypt(key_name)
            api_url =  "%s/create" % self.hash_table.get(partition)
            response_partition = requests.post(api_url, json={"key": key, "value": value})
            if(response_partition.json() != None):
                response_replication = self.replication(key_hash, value)
                if(self.current_partition >= self.partition_number):
                    self.current_partition = 1
                else:
                    self.current_partition += 1
                return {
                    "id": key_hash,
                    "message": "Sucess save key/value",
                    "status": True,
                    "replication": response_replication
                }
            else:
                return {
                    "message": "Error saving key/value",
                    "status": False
                } 
                
        except(e):
            return {
                "message": "Id error value",
                "status": False
            }

    def find_by_id(self, id):
        try:
            decrypted_data = self.decrypt(id).split(":")
            partition = decrypted_data[0]
            key = decrypted_data[1]
            partition_replication_number = int(''.join(filter(str.isdigit, partition))) + 1
            partition_replication =  "partition%s" % (partition_replication_number, 1)[partition_replication_number > self.partition_number]
            api_url = self.hash_table.get(partition) + "/get/" + key
            api_url_replication = self.hash_table.get(partition_replication) + "/get/" + key
            response = requests.get(api_url)
            response_replication = requests.get(api_url_replication)
            if(response.json() != None and response_replication.json() != None):
                return {
                    "key": key,
                    "value": response.json() ,
                    "message": "Sucess save key/value",
                    "status": True,
                    "replication": True
                }
            elif (response.json()):
                return {
                    "key": key,
                    "value": response.json(),
                    "message": "Sucess save value only on main",
                    "status": True,
                    "replication": False
                }
            elif(response_replication.json()):
                return {
                    "key": key,
                    "value": response_replication.json(),
                    "message": "Sucess save value only on replica",
                    "status": False,
                    "replication": True
                }
            else:
                return {
                    "message": "Error getting key/value",
                    "status": False
                }

        except(err):
            return {
                "message": "Id error value",
                "status": False
            }

    def update_by_id(self, id, value):
        try:
            decrypted_data = self.decrypt(id).split(":")
            partition = decrypted_data[0]
            partition_replication_number = int(''.join(filter(str.isdigit, partition))) + 1
            partition_replication = "partition%s" % (partition_replication_number, 1)[partition_replication_number > self.partition_number]
            api_url = self.hash_table.get(partition) + "/update"
            api_url_replication = self.hash_table.get(partition_replication) + "/update"
            response = requests.put(api_url, json={"key": id, "value": value})
            response_replication = requests.put(api_url_replication, json={"key": id, "value": value})
            print(response.json())
            if(response.json() != None and response_replication.json() != None):
                return {
                    "message": "Sucess update value and replication",
                    "status": True,
                    "replication": True
                }
            elif (response.json()):
                return {
                    "message": "Sucess update value only on main",
                    "status": True,
                    "replication": False
                }
            elif(response_replication.json()):
                return {
                    "message": "Sucess update value only on replica",
                    "status": False,
                    "replication": True
                }
            else:
                return {
                    "message": "Error updating key/value",
                    "status": False
                }

        except(err):
            return {
                "message": "Id error value",
                "status": False
            }

    def delete_by_id(self, id):
        try:
            decrypted_data = self.decrypt(id).split(":")
            partition = decrypted_data[0]
            key = decrypted_data[1]
            partition_replication_number = int(''.join(filter(str.isdigit, partition))) + 1
            partition_replication = "partition%s" % (partition_replication_number, 1)[partition_replication_number > self.partition_number]
            api_url = self.hash_table.get(partition) + "/delete/" + key
            api_url_replication = self.hash_table.get(partition_replication) + "/delete/"+key
            response = requests.delete(api_url)
            response_replication = requests.delete(api_url_replication)
            if(response.json() != None and response_replication.json() != None):
                return {
                    "message": "Sucess delete key/value",
                    "status": True,
                    "replication": True
                }
            elif (response.json()):
                return {
                    "message": "Sucess delete value only on main",
                    "status": True,
                    "replication": False
                }
            elif(response_replication.json()):
                return {
                    "message": "Sucess delete value only on replica",
                    "status": False,
                    "replication": True
                }
            else:
                return {
                    "message": "Error deleting key/value",
                    "status": False
                }

        except(err):
            return {
                "message": "Id error value",
                "status": False
            }
    
    def set_hash(self, hash):
        try: 
            path_couter = 1
            
            self.partition_number = int(hash.partition_number)
            self.hash_table = HashTable(self.partition_number)
                        
            while(path_couter <= self.partition_number):
                path_name = "PATH_%s" % path_couter
                partition_name = "partition%s" % path_couter
                partition_url = hash.value[partition_name]
                self.hash_table.append(partition_name, partition_url)
                response = requests.post(partition_url+"/setPath", json={"path_name":path_name } )
                path_couter = path_couter + 1
                
                
            return {
                "message": "test"
                
            }
        except(e):
            return {
                "message": "Id error value",
                "status": False
            }
        

    def encrypt(self, text):
        return self.fernet.encrypt(text.encode()).decode('utf8')

    def decrypt(self,text):
        return self.fernet.decrypt(text).decode()
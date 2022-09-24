from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from hashTable import HashTable
import requests


class routingTier:

    def __init__(self, partitions_number):
        key_name = 'proyecto1'.encode("ascii")
        self.current_partition = 0
        self.partition_number = partitions_number
        self.hash_table = HashTable(partitions_number)
        self.key_buffer = PBKDF2(
            key_name, key_name, 32, count=1000, hmac_hash_module=SHA256)

    def create_key_value(self, key, value):
        key_name = 'partition' + self.current_partition + ":" + key
        key_hash = self.encrypt(key_name)
        api_url = self.hash_table.get(
            'partition' + self.current_partition) + "/records/create"
        response = requests.post(api_url, json={key: key_hash, value: value})
        if(response.json()):
            if(self.current_partition >= self.partition_number):
                self.current_partition = 0
            else:
                self.current_partition += 1
            return {
                "id": key_hash,
                "message": "Sucess save key/value",
                "status": False
            }
        else:
            return {
                "message": "Error saving key/value",
                "status": False
            }

    def find_by_id(self, id):
        try:
            decrypted_data = self.decrypt(id).split(":")
            partition = decrypted_data[0]
            api_url = self.hash_table.get(partition) + "/records/get/" + id
            response = requests.get(api_url)
            if(response.json()):
                return {
                    "key": key,
                    "value": response.json(),
                    "message": "Sucess save key/value",
                    "status": True
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
            api_url = self.hash_table.get(partition) + "/records/update"
            response = requests.get(api_url, json={"key": id, "value": value})
            if(response.json()):
                return {
                    "message": "Sucess update value",
                    "status": True
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

    def delete_by_key(self, id):
        try:
            decrypted_data = self.decrypt(id).split(":")
            partition = decrypted_data[0]
            api_url = self.hash_table.get(partition) + "/records/delete/"+id
            response = requests.delete(api_url)
            if(response.json()):
                return {
                    "message": "Sucess delete key/value",
                    "status": True
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

    def resize_length(self, string):
        # resizes the String to a size divisible by 16 (needed for this Cipher)
        return string.rjust((len(string) // 16 + 1) * 16)

    def encrypt(self, url):
        # Converts the string to bytes and encodes them with your Cipher
        cipher = AES.new(self.key_buffer, AES.MODE_CBC)
        self.iv = cipher.iv
        return cipher.encrypt(self.resize_length(url).encode())

    def decrypt(self, text):
        # Converts the string to bytes and decodes them with your Cipher
        cipher = AES.new(self.key_buffer, AES.MODE_CBC)
        return cipher.decrypt(text).decode().lstrip()

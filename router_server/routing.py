from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from hashTable import HashTable
import requests
import json


class routingTier:

    def __init__(self, partitions_number):
        key_name = 'proyecto1'.encode("ascii")
        self.hash_table = HashTable(partitions_number)
        self.key_buffer = PBKDF2(
            key_name, key_name, 32, count=1000, hmac_hash_module=SHA256)

    def create_key_value(self, key, value):
        encrypted_key = self.encrypt(json.dumps(key))
        key_object = ""
        print(key['key'])
        self.hash_table.append(encrypted_key, "http://52.204.153.196")
        api_url = self.hash_table.get(encrypted_key) + "/records/create"
        response = requests.post(api_url, json={"key": key['key'], "value": value})
        print(response.json())
        bucket = self.hash_table.get_bucket(encrypted_key)
        print(bucket)
        for index, record in enumerate(bucket):
            print(record)
        return

    def find_by_key(self, key):
        key_object = eval(self.decrypt(key))
        """ node_dir = self.hash_table.get(key_object.node)
        partition_number = key_object.partition
        key_value = key_object.partition """

        print(key_object)

    def update_by_key(self, key, value):
        return

    def delete_by_key(self, key, value):
        return

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


router = routingTier(50)
dict = {"node": 1231, "partition": 1, "key": "key"}
router.create_key_value(dict, "noname")
""" router.findFile(test) """

""" router.findFile(test) """

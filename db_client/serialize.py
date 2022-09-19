import pickle
from hashing256 import Hashing256

class serialize:

    def __init__(self):
        self.hashing = Hashing256()

    def write_record(self, key, value):
        records = self.read_records()
        outfile = open('records', 'wb')
        try:
            if(records == {}):
                records = {self.hashing.generate_hash(key): value}
            elif (records[self.hashing.generate_hash(key)] == None):
                records[self.hashing.generate_hash(key)] = value
        except KeyError:
            records[self.hashing.generate_hash(key)] = value

        pickle.dump(records, outfile)
        outfile.close()
        return True

    def read_records(self):
        records = {}
        try:
            infile = open('records', 'rb')
            records = pickle.load(infile)
            infile.close()
        except FileNotFoundError:
            records = {}
        return records

    def search_record(self, key):
        records = self.read_records()
        try:
            value = records[self.hashing.generate_hash(key)]
            if (value != None):
                return value
        except KeyError:
            return False

    def update_record(self, key, value):
        records = self.read_records()
        outfile = open('records', 'wb')
        try:
            if (records[self.hashing.generate_hash(key)] != None):
                records[self.hashing.generate_hash(key)] = value
        except KeyError:
            return False

        pickle.dump(records, outfile)
        outfile.close()

        return True

    def delete_record(self, key):
        records = self.read_records()
        outfile = open('records', 'wb')
        try:
            if (records[self.hashing.generate_hash(key)] != None):
                del records[self.hashing.generate_hash(key)]
        except KeyError:
            return False

        pickle.dump(records, outfile)
        outfile.close()

        return True

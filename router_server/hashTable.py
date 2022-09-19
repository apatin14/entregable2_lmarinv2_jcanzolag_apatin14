class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def get_bucket(self, key):
        return self.hash_table[hash(key) % self.size]

    def append(self, key, val):
        bucket = self.hash_table[hash(key) % self.size]
        found_key, index, record_val = self.is_key(bucket, key)
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def get(self, key):
        bucket = self.hash_table[hash(key) % self.size]
        found_key, index, record_val = self.is_key(bucket, key)
        if found_key:
            return record_val
        else:
            return "No record found"

    def delete(self, key):
        bucket = self.hash_table[hash(key) % self.size]
        found_key, index, record_val = self.is_key(bucket, key)
        if found_key:
            bucket.pop(index)
        return

    def is_key(self, bucket, key):
        found_key = False
        index = None
        record_val = None
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                index = index
                record_val = record_val
                break
        return (found_key, index, record_val)

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

# hastable
class HashTable:

    # constructor inits hash table with lists
    # O(n) or O(1)
    def __init__(self, cap=10):
        self.table = []
        for _ in range(cap):
            self.table.append([])
    # O(1)
    def create_hash(self, data_key):
        return int(data_key) % len(self.table)

    # function that adds new data into hash table
    # O(n)
    def add(self, data_key, data):
        # identifying the bucket list position to add the new data
        bucket = self.create_hash(data_key)
        bucket_list = self.table[bucket]
        
        # update data_key if already present
        for key_value in bucket_list:
            if key_value[0] == data_key:
                key_value[1] = data
                return
        # add the new data_key and data to the bucket_list
        key_value = [data_key, data]
        bucket_list.append(key_value)
        return 
  
    # searching for a data matching with the data_key in the hash table
    # O(n)
    def search(self, data_key):
        # find which bucket the data_key is in
        bucket = self.create_hash(data_key)
        bucket_list = self.table[bucket]

        # if the data_key matches with key_value[0] 
        # then return the data else None
        for key_value in bucket_list:
            if key_value[0] == data_key:
              return key_value[1]
        return None

    # remove a data matching with the data_key in the hash table
    # O(n)
    def remove(self, data_key):
        # find which bucket the data_key is in
        bucket = self.create_hash(data_key)
        bucket_list = self.table[bucket]

        # if the data_key matches the key_value[0]
        # then remove the key value pair from the bucket_list
        # else return None
        for key_value in bucket_list:
            if key_value[0] == data_key:
              bucket_list.remove([key_value[0], key_value[1]])
            else:
              print("The data key does not exist")

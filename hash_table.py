# hastable
class HashTable:

    # constructor inits hash table with lists
    def __init__(self, cap=10):
        self.table = []
        for _ in range(cap):
            self.table.append([])

    # function that adds new data into hash table
    """def add(self, data):
				# identifying the bucket position to add the new data
				bucket = hash(data) % len(self.table)
				bucket_list = self.table[bucket]
				# adding the data
				bucket_list.append(data)"""

    # function that adds new data into hash table
    def add(self, data_key, data):
        # identifying the bucket list position to add the new data
        bucket = hash(data_key) % len(self.table)
        bucket_list = self.table[bucket]

        # update data_key if already present
        for key_value in bucket_list:
            print(key_value)

    """
		# searching for a data matching with the data_key in the hash table
		def search(self, data_key):
				# find which bucket the data_key is in
				bucket = hash(data_key) % len(self.table)
				bucket_list = self.table[bucket]

				# if the data_key is found then return the the data else none
				if data_key in bucket_list:
						data_key_index = bucket_list.index(data_key)
						return bucket_list[data_key_index]
				else:
						return None

		# remove a data matching with the data_key in the hash table
		def remove(self, data_key):
				# find which bucket the data_key is in
				bucket = hash(data_key) % len(self.table)
				bucket_list = self.table[bucket]

				# now remove it
				if data_key in bucket_list:
						bucket_list.remove(data_key)
"""


myHashTable = HashTable()

myHashTable.add("Tapa")
print(myHashTable.table)
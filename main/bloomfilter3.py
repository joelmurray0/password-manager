import hashlib
import numpy as np
#from binary_to_bytes import binary_to_bytes

# class BloomFilter():
#      def __init__(self, size, hash1, hash2, name):
#           self.size = size*8 # can only store in bytes so that is the requirement going in
#           self.name = name
          
#           np.savetxt(f"{name}.npy", self.filter, fmt="%.1f")
#           self.hash1 = hash1
#           self.hash2 = hash2
     
def find_hash_index(data, hash1, hash2, size): # prone to error if the hashes are changed
     # Turns string into bytes
     data = data.encode()
     # Creates instances of the hash functions and adds the data
     h1 = hashlib.new(hash1)
     h2 = hashlib.new(hash2)
     h1.update(data)
     h2.update(data)
     # Returns index from the resulting hash
     return int.from_bytes(h1.digest(), "little") % size, int.from_bytes(h2.digest(), "little") % size

def open(name, size):
     try:
          filter = np.load(f"{name}.npy")
     except Exception:
          filter = np.zeros(size)
     return filter

def add_to_bloom_filter(name, data, hash1, hash2, size):
     filter = open(name)
     # Returns index values of the data from the two hashes
     i1, i2 = find_hash_index(data)
     # Assigns 1 to the indexes
     filter[i1] = 1
     filter[i2] = 1
     print(filter)
     np.save(f"{name}.npy", filter)

def data_exists(name, data):
     i1, i2 = find_hash_index(data)
     # Checks to see if data is in the set
     array = open(name)
     return array[i1] == 1 and array[i2] == 1

# bloom_filter = BloomFilter(256, "sha256", "sha3_256")

# bloom_filter.add_to_bloom_filter("bloomfilter", "password")
# bloom_filter.add("gimme")
# bloom_filter.write()
# print(bloom_filter.data_exists("gimme"))

# print(bloom_filter.filter)

add_to_bloom_filter("bloomfilter.txt", )
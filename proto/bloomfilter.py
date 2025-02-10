import hashlib
import numpy as np

class BloomFilter():
     def __init__(self, size, hash1, hash2):
          self.size = size
          self.filter = np.zeros(self.size)
          self.hash1 = hash1
          self.hash2 = hash2\
     
     def find_hash_index(self, data):
          # Turns string into bytes
          data = data.encode()
          # Creates instances of the hash functions and adds the data
          h1 = hashlib.new(self.hash1)
          h2 = hashlib.new(self.hash2)
          h1.update(data)
          h2.update(data)
          # Returns index from the resulting hash
          return int.from_bytes(h1.digest(), "little") % self.size, int.from_bytes(h2.digest(), "little") % self.size


     def add(self, data):
          # Returns index values of the data from the two hashes
          i1, i2 = self.find_hash_index(data)
          # Assigns 1 to the indexes
          self.filter[i1] = 1
          self.filter[i2] = 1
    
     def data_exists(self, data):
          i1, i2 = self.find_hash_index(data)
          # Checks to see if data is in the set
          return self.filter[i1] == 1 and self.filter[i2] == 1
        

bloom_filter = BloomFilter(256, "sha256", "sha3_256")

bloom_filter.add("password")
bloom_filter.add("gimme")
print(bloom_filter.data_exists("gibb"))

print(bloom_filter.filter)
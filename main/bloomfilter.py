import numpy as np
import hashlib
import pickle

class BloomFilter:
    def __init__(self, size: int, hash_count: int):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = np.zeros(size, dtype=bool)
    
    def _hashes(self, item: str):
        hash_values = []
        for i in range(self.hash_count):
            hash_val = int(hashlib.md5(f"{item}{i}".encode()).hexdigest(), 16)
            hash_values.append(hash_val % self.size)
        return hash_values
    
    def add(self, item: str):
        for index in self._hashes(item):
            self.bit_array[index] = True
    
    def contains(self, item: str) -> bool:
        return all(self.bit_array[index] for index in self._hashes(item))
    
    def __contains__(self, item: str) -> bool:
        return self.contains(item)
    
    def save(self, filename: str):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
    
    @staticmethod
    def load(filename: str):
     try:
          with open(filename, 'rb') as f:
               return pickle.load(f)
     except Exception:
          return BloomFilter(size=1000, hash_count=5)

# Example usage:
bf = BloomFilter.load("password_bloom_filter.pkl")

# result = bf.__contains__("qwerty")
# print()
# print(result)
#bf.add("hello")
#bf.save("bloom_filter.pkl")

# with open("bad_passwords.txt", "r") as f:
#      for i in f.readlines():
#           bf.add(i)
#      bf.save("password_bloom_filter.pkl")

# with open("bad_passwords.txt", "r") as f:
#     for i in f.readlines():
#         temp = bf.__contains__(i)
#         print(temp)

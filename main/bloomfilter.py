import os
import numpy as np
import hashlib
import pickle

class BloomFilter:
    def __init__(self, size: int):
        self.size = size
        self.bit_array = np.zeros(size, dtype=bool)
    
    def _hashes(self, item: str):
        hash_val_1 = int(hashlib.md5(item.encode()).hexdigest(), 16) % self.size
        hash_val_2 = int(hashlib.sha256(item.encode()).hexdigest(), 16) % self.size
        return [hash_val_1, hash_val_2]
    
    def add(self, item: str):
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = True
    
    def check_not_in(self, item: str) -> bool:
        for hash_index in self._hashes(item):
            if self.bit_array[hash_index] == False:
                return True
        return False

    def save(self, filename: str):
        folder = "bloomfilter"
        if not os.path.exists(folder):
            os.makedirs(folder)  # Create the directory if it doesn't exist
            
        with open(os.path.join('bloomfilter', filename), 'wb') as f:
            pickle.dump(self, f)
    
    @classmethod
    def load(cls, filename: str):
        # print(os.path.exists(os.path.join("bloomfilter", f"{filename}.pkl")))
        if not os.path.exists(os.path.join("bloomfilter", f"{filename}.pkl")):
            # File doesn't exist, create a new BloomFilter with default values
            bloom_filter = cls(size=10000)
            # Optionally save this new filter to the file for future use
            # bloom_filter.save(filename)
        else:
            print("file exists")
            with open(os.path.join('bloomfilter', f"{filename}.pkl"), 'rb') as f:
                bloom_filter = pickle.load(f)
                print(bloom_filter.bit_array)
            return bloom_filter
        return bloom_filter

        # try:
        #     with open(os.path.join('bloomfilter', filename), 'rb') as f:
        #         return pickle.load(f)
        # except Exception:
        #     return BloomFilter(size=1000, hash_count=5)

# Example usage:
bf = BloomFilter(10000)

# result = bf.__contains__("qwerty")
# print()
# print(result)
#bf.add("hello")
#bf.save("bloom_filter.pkl")

# with open("bad_passwords.txt", "r") as f:
#     lines = f.readlines()
#     for i in lines:
#         # print(i.rstrip("\n"))
#         bf.add(i.rstrip("\n"))
#     #print(lines)
#     bf.save("password_bloom_filter.pkl")

# with open("bad_passwords.txt", "r") as f:
#     for i in f.readlines():
#         temp = bf.__contains__(i)
#         print(temp)

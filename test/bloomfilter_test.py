from main.bloomfilter import BloomFilter, np, os
import pytest

@pytest.fixture(autouse=True)
def setup():
     file_path = os.path.join("bloomfilter", "test_filter.pkl")

     # Check if the file exists before deleting
     if os.path.exists(file_path):
          os.remove(file_path)

def test__hashes():
     bloom_filter = BloomFilter(10)
     results = bloom_filter._hashes("hello")
     assert len(results) == 2
     assert results[0] != results[1] != "hello"

def test_add():
     bloom_filter = BloomFilter(10)
     bloom_filter.add("hello")
     assert not np.array_equal(bloom_filter.bit_array, np.zeros(bloom_filter.size, dtype=bool))

def test_check_not_in():
     bloom_filter = BloomFilter(10)
     bloom_filter.add("hello")
     assert not bloom_filter.check_not_in("hello")
     assert bloom_filter.check_not_in("helli")

def test_load_can_create_file_if_one_does_not_exist():
     bloom_filter = BloomFilter.load("test_filter") # this file does not exist
     assert bloom_filter.size == 10000
     assert np.array_equal(bloom_filter.bit_array, np.zeros(bloom_filter.size, dtype=bool))

def test_save():
     filename = "test_filter"
     bloom_filter = BloomFilter.load(filename)
     bloom_filter.save(filename)
     with open(os.path.join("bloomfilter", filename), "rb") as file:
          content = file.read() 
          assert isinstance(content, bytes)
          assert len(content) != 0

def test_load_can_find_pre_existing_file(): # scammed
     filename = "test_filter"
     bloom_filter = BloomFilter.load(filename)
     bloom_filter.add("world")
     bloom_filter.save(filename)
     new_bloom_filter = BloomFilter.load(filename)

     print(bloom_filter.bit_array)
     print(new_bloom_filter.bit_array)

     #assert not new_bloom_filter.check_not_in("world")
     assert new_bloom_filter.check_not_in("word")
     assert bloom_filter.bit_array.all() == new_bloom_filter.bit_array.all()
     assert bloom_filter.size == new_bloom_filter.size
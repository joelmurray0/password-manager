from main.bloomfilter import BloomFilter, np, os


def test__hashes():
     bloom_filter = BloomFilter(10, 2)
     results = bloom_filter._hashes("hello")
     assert len(results) == 2
     assert results[0] != results[1] != "hello"

def test_add():
     bloom_filter = BloomFilter(10, 2)
     bloom_filter.add("hello")


def test_contains():
     bloom_filter = BloomFilter(10, 2)
     bloom_filter.add("hello")
     assert bloom_filter.contains("hello")

def test___contains__():
     bloom_filter = BloomFilter(10, 2)
     bloom_filter.add("hello")
     assert "hello" in bloom_filter

def test_load_can_create_file_if_one_does_not_exist():
     bloom_filter = BloomFilter.load("test_filter") # this file does not exist
     assert bloom_filter.size == 1000
     assert bloom_filter.hash_count == 5
     assert bloom_filter.bit_array.all() == np.zeros(bloom_filter.size, dtype=bool).all()

def test_save():
     filename = "test_filter"
     bloom_filter = BloomFilter.load(filename)
     bloom_filter.save(filename)
     with open(os.path.join("bloomfilter", filename), "rb") as file:
          content = file.read() 
          assert isinstance(content, bytes)
          assert len(content) != 0

def test_load_can_find_pre_existing_file():
     filename = "test_filter"
     bloom_filter = BloomFilter.load(filename)
     bloom_filter.add("world")
     bloom_filter.save(filename)
     new_bloom_filter = BloomFilter.load(filename)
     assert "world" in new_bloom_filter
     assert bloom_filter.bit_array.all() == new_bloom_filter.bit_array.all()
     assert bloom_filter.hash_count == new_bloom_filter.hash_count
     assert bloom_filter.size == new_bloom_filter.size
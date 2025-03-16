from main.utilities.tokeniser import *

def test_fuzzy_search_insertions():
     results = generate_fuzzy_insertions("a")
     assert "aa" in results
     assert "za" in results
     assert "ab" in results
     assert "az" in results

def test_fuzzy_search_substitutions():
     results = generate_fuzzy_substitutions("a")
     assert not "a" in results
     assert "b" in results
     assert "z" in results

def test_fuzzy_search_deletions():
     results = generate_fuzzy_deletions("a")
     assert [""] == results

def test_n_grams_within_word_length():
     result = generate_ngrams("abc", 2)
     assert result == ["ab", "bc"]

def test_n_grams_for_larger_than_word_length():
     result = generate_ngrams("abc", 4)
     assert result == []

def test_variable_n_grams_2_to_6():
     result = generate_variable_ngrams("eletters")
     for i in result:
          assert 2 <= len(i) <= 6
     
def test_variable_n_grams_stays_within_word_size():
     result = generate_variable_ngrams("hello")
     for i in result:
          assert 2 <= len(i) <= len("hello")

def test_variable_n_grams_stays_within_word_size_outside_of_normal_limit():
     result = generate_variable_ngrams("letters", 2, 8)
     for i in result:
          assert 2 <= len(i) <= len("letters")
          assert not len("letters") < len(i[0]) <= 8

def test_generate_tokens():
     result = generate_tokens("hello", 1)
     test = []
     for i in result:
          assert i[-1] == 1
          test.append(i[0])
     assert len(test) == len(set(test))
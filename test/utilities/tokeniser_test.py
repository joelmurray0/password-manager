from main.utilities.tokeniser import *

def test_url_works_subdomain_www():
     results = extract_url_parts(url="http://www.abc.com/suckmy", id=0)
     check = []
     for result in results:
          check.append(result[0])
     print(check)
     assert set(check) == set(["abc", "abc.com", "suckmy"])

def test_url_works_with_no_head():
     results = extract_url_parts(url="google.com", id=0)
     check = []
     for result in results:
          check.append(result[0])
     print(check)
     assert set(check) == set(["google", "google.com", "com"])


def test_url_works_subdomain_no_www():
     results = extract_url_parts(url="http://subby.ttt.co.uk/plop?a=r", id=0)
     print(results)
     check = []
     for result in results:
          check.append(result[0])
     assert check == ['ttt', 'subby.ttt.co.uk', 'ttt.co.uk', 'subby', 'plop']
# subby, ttt, ttt.co.uk, subby.ttt.co.uk, plop

# def test_fuzzy_search_insertions():
#      results = generate_fuzzy_insertions("a")
#      assert "aa" in results
#      assert "za" in results
#      assert "ab" in results
#      assert "az" in results

# def test_fuzzy_search_substitutions():
#      results = generate_fuzzy_substitutions("a")
#      assert not "a" in results
#      assert "b" in results
#      assert "z" in results

# def test_fuzzy_search_deletions():
#      results = generate_fuzzy_deletions("a")
#      assert [""] == results

# def test_n_grams_within_word_length():
#      result = generate_ngrams("abc", 2)
#      assert result == ["ab", "bc"]

# def test_n_grams_for_larger_than_word_length():
#      result = generate_ngrams("abc", 4)
#      assert result == []

# def test_variable_n_grams_2_to_6():
#      result = generate_variable_ngrams("eletters")
#      for i in result:
#           assert 2 <= len(i) <= 6
     
# def test_variable_n_grams_stays_within_word_size():
#      result = generate_variable_ngrams("hello")
#      for i in result:
#           assert 2 <= len(i) <= len("hello")

# def test_variable_n_grams_stays_within_word_size_outside_of_normal_limit():
#      result = generate_variable_ngrams("letters", 2, 8)
#      for i in result:
#           assert 2 <= len(i) <= len("letters")
#           assert not len("letters") < len(i[0]) <= 8

# def test_generate_tokens():
#      result = generate_tokens("hello", 1)
#      test = []
#      for i in result:
#           assert i[-1] == 1
#           test.append(i[0])
#      assert len(test) == len(set(test))

# http://www.abc.com/suckmy

# 

# 

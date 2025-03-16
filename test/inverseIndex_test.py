from inverseIndex import InverseIndex

def test_add():
     inverse_index = InverseIndex()
     inverse_index.add("string", 1)
     assert inverse_index.head.data == ['string', [1]]
     assert inverse_index.head.next == None

def test_add_to_end():
     inverse_index = InverseIndex()
     inverse_index.add("stringa", 1)
     inverse_index.add("stringb", 2)
     temp = inverse_index.head
     assert temp.data == ['stringa', [1]]
     temp = temp.next
     assert temp.data == ['stringb', [2]]
     temp = temp.next
     assert temp == None

def test_adding_sorts():
     inverse_index = InverseIndex()
     inverse_index.add("string", 1)
     inverse_index.add("astring", 2)
     temp = inverse_index.head
     assert temp.data == ['astring', [2]]
     temp = temp.next
     assert temp.data == ['string', [1]]
     temp = temp.next
     assert temp == None

def test_adding_same_string_with_different_index_merges():
     inverse_index = InverseIndex()
     inverse_index.add("string", 1)
     inverse_index.add("string", 2)
     temp = inverse_index.head
     assert temp.data == ['string', [1, 2]] 
     assert temp.next == None

def test_adding_same_string_with_same_index_merges():
     inverse_index = InverseIndex()
     inverse_index.add("string", 1)
     inverse_index.add("string", 1)
     temp = inverse_index.head
     assert temp.data == ['string', [1]] 
     assert temp.next == None

def test_adding_same_string_with_same_index_merges_not_in_first_position_of_list():
     inverse_index = InverseIndex()
     inverse_index.add("a", 0)
     inverse_index.add("string", 1)
     inverse_index.add("string", 1)
     temp = inverse_index.head
     assert temp.data == ['a', [0]] 
     temp = temp.next
     assert temp.data == ['string', [1]]
     assert temp.next == None

def test_remove_leaves_no_empty_index_or_index_with_removed_id():
     num = 1
     inverse_index = InverseIndex()
     inverse_index.add("string", num)
     inverse_index.add("string", 2)
     inverse_index.add("text", num)
     inverse_index.delete(num)
     temp = inverse_index.head
     while temp.next != None:
          assert temp.data[1] != [] and num not in temp.data[1]
          temp = temp.next
          

def test_search_exact_term_returns_term_first():
     inverse_index = InverseIndex()
     inverse_index.add("string", 1)
     assert inverse_index.search("string")[0] == 1

# def test_search_one_letter_extra_found():
#      inverse_index = InverseIndex()
#      inverse_index.add("stringg", 1)
#      assert inverse_index.search("string")[0] == 1

# def test_search_one_letter_substituted_found():
#      inverse_index = InverseIndex()
#      inverse_index.add("strinj", 1)
#      assert inverse_index.search("string")[0] == 1

# def test_search_one_letter_removed_found():
#      inverse_index = InverseIndex()
#      inverse_index.add("strig", 1)
#      assert inverse_index.search("string")[0] == 1

# def test_range_given_back():
#      inverse_index = InverseIndex()
#      inverse_index.add("a", 1)
#      inverse_index.add("b", 2)
#      inverse_index.add("c", 3)
#      inverse_index.add("d", 4)
#      inverse_index.add("e", 5)
#      inverse_index.add("ab", 6)
#      inverse_index.add("az", 7)
#      assert set(inverse_index.range_search("a")) == set([1,6,7])
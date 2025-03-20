from inverseIndex import InverseIndex

def test_add():
     inverse_index = InverseIndex()
     inverse_index.add("string", [1])
     assert inverse_index.head.data == ['string', [1]]
     assert inverse_index.head.next == None

def test_add_to_end():
     inverse_index = InverseIndex()
     inverse_index.add("stringa", [1])
     inverse_index.add("stringb", [2])
     temp = inverse_index.head
     assert temp.data == ['stringa', [1]]
     temp = temp.next
     assert temp.data == ['stringb', [2]]
     temp = temp.next
     assert temp == None

def test_adding_sorts():
     inverse_index = InverseIndex()
     inverse_index.add("string", [1])
     inverse_index.add("astring", [2])
     temp = inverse_index.head
     assert temp.data == ['astring', [2]]
     temp = temp.next
     assert temp.data == ['string', [1]]
     temp = temp.next
     assert temp == None

def test_adding_sorts_positions_first_middle_last():
     inverse_index = InverseIndex()
     inverse_index.add("c", [1])
     inverse_index.add("e", [1])
     inverse_index.add("a", [1])
     inverse_index.add("d", [1]) # middle
     inverse_index.add("f", [1])
     inverse_index.display()
     temp = inverse_index.head
     assert temp.data[0] == "a"
     temp = temp.next
     assert temp.data[0] == "c"
     temp = temp.next
     assert temp.data[0] == "d"
     temp = temp.next
     assert temp.data[0] == "e"
     temp = temp.next
     assert temp.data[0] == "f"
     assert not temp.next 


def test_adding_same_string_with_different_index_merges():
     inverse_index = InverseIndex()
     inverse_index.add("string", [1])
     inverse_index.add("string", [2])
     temp = inverse_index.head
     assert temp.data == ['string', [1, 2]] 
     assert temp.next == None

def test_adding_same_string_with_same_index_merges():
     inverse_index = InverseIndex()
     inverse_index.add("string", [1])
     inverse_index.add("string", [1])
     temp = inverse_index.head
     assert temp.data == ['string', [1]] 
     assert temp.next == None

def test_adding_same_string_with_same_index_merges_not_in_first_position_of_list():
     inverse_index = InverseIndex()
     inverse_index.add("a", [0])
     inverse_index.add("string", [1])
     inverse_index.add("string", [1])
     temp = inverse_index.head
     assert temp.data == ['a', [0]] 
     temp = temp.next
     assert temp.data == ['string', [1]]
     assert temp.next == None

def test_remove_leaves_no_empty_index_or_index_with_removed_id():
     num = 1
     inverse_index = InverseIndex()
     inverse_index.add("string", [num])
     inverse_index.add("string", [2])
     inverse_index.add("text", [num])
     inverse_index.delete(num)
     temp = inverse_index.head
     while temp.next != None:
          assert temp.data[1] != [] and num not in temp.data[1]
          temp = temp.next
          

def test_search_exact_term_returns_term_first():
     inverse_index = InverseIndex()
     inverse_index.add("string", [1])
     assert inverse_index.search("string")[0] == 1


def test_search_element_finds_element():
     inverse_index = InverseIndex()
     inverse_index.add("string", [1])
     inverse_index.add("string", [2])
     assert inverse_index.search("string") == [1,2]

def test_search_with_multiple_elements():
     inverse_index = InverseIndex()
     inverse_index.add("string", [1])
     inverse_index.add("strings", [2])
     assert inverse_index.search("string") == [1]
     assert inverse_index.search("strings") == [2]

def test_search_with_multiple_elements_multiple_ids():
     inverse_index = InverseIndex()
     inverse_index.add("string", [1])
     inverse_index.add("strings", [2])
     inverse_index.add("strings", [3])
     assert inverse_index.search("string") == [1]
     assert inverse_index.search("strings") == [2, 3]

def test_two_creates_with_same_arr_diff_order_create_same_inverse_index():
     inverse_index_1 = InverseIndex(arr=[["a", [1]], ["b", [1,2]]])
     inverse_index_2 = InverseIndex(arr = [["b", [1,2]], ["a", [1]]])

     assert inverse_index_1.save() == inverse_index_2.save()
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
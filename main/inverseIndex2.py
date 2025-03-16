# from mergesort import merge_sort
# import string
# from metaphone import doublemetaphone
# from symspellpy import SymSpell, Verbosity
# from fuzzy import Soundex
# from Levenshtein import editops, distance
# import itertools
# from utilities.tokeniser import generate_edits, generate_variable_ngrams
# from binarysearcharr2d import binary_search_arr2d

# class InverseIndex:
#      def __init__(self):
#           self.token_table = []

     
#      def add(self, string, id):
#           # create partials tokens
#           # adds tokens to token table - it is now unsorted
#           # all tokens are lowercase
#           # try:
#           #      self.token_dict[id].append(string)
#           # except KeyError:
#           #      self.token_dict[id] = [string]

#           # sorts token table
#           duplicated_token_table = merge_sort(self.token_table)
#           self.token_table = self.unduplicate_2d_arr(duplicated_token_table)
#           self.reverse_token_table = merge_sort(self.reverse_table(self.token_table))
          

#      def remove(self, id):
#           pass

#      def unduplicate_2d_arr(self, arr2d):
#           temp_dict = {}
#           for i in arr2d:
#                if i[0] in temp_dict:
#                     current = temp_dict[i[0]]
#                     list(set(current.extend(i[1]))) # work on this so no duplicates also check if there are IDKKK
#                     temp_dict[i[0]] = current
#                else:
#                     temp_dict[i[0]] = i[1]
#           return [[key, value] for key, value in temp_dict.items()]

#      def remove_tokens(self, id):
#           i=0
#           while i < len(self.token_table):
#                if id in self.token_table[i][1]:
#                     self.token_table[i][1].remove(id)
#                     if self.token_table[i][1] == []:
#                          self.token_table.pop(i)
#                          i -= 1
#                i += 1
          
#      def search(self, query, reverse=False):
#           search_ids = []

#           if reverse:    
#                binary_search_arr2d(self.reverse_token_table, query)
#           else:
#                pass
     
#      # def basic_search(self, query):
#      #      search_ids = []

#      #      phonetic_code = doublemetaphone(query)[0] # searches as if user put in something similar phonetically - set should be small enough to be useful
#      #      search_ids.extend([word[1] for word in self.token_table if doublemetaphone(word[0])[0] == phonetic_code]) # return search ids
          
#      #      return self.token_table[binary_search_arr2d(self.token_table, query)][1] #returns id found in search -- instead of  binary seraching do levenshtein distance for top results
          
          

          


# # is it more efficient to reverse the whole fully sorted list than reverse and order the new elements and add those to the table as that takes 2 merge sorts instead of using once and then O(n) flipping process
# # especially the more complex the systems get for tokens

#      def reverse_table(self):
#           output = []
#           for i in self._token_table[::-1]:
#                temp = [i[0][::-1], i[1]]
#                output.append(temp)
#           return output






# if search_ids == []:
#                     sym_spell = SymSpell(max_dictionary_edit_distance=2)
#                     sym_spell.load_dictionary("frequency_dictionary_en_82_765.txt", 0, 1)
#                     suggestions = sym_spell.lookup(query, Verbosity.CLOSEST, max_edit_distance=2) # might miscorrect important words like com --> come maybe apply if none found before
#                     if suggestions:
#                          corrected_query = suggestions[0].term
#                     else:
#                          pass # no more search to occur - nothing found
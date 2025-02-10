import pickle
from encryption import aes_decrypt_data, aes_encrypt_data, hash
from key import derive_key
from vaultItem import VaultItem
import string
from prettytable import PrettyTable

class Vault:
     def __init__(self, name, master_password):
          self._name = name
          self.items = {}
          self.removed = []
          self._token_table = []
          self.check = aes_encrypt_data(derive_key(master_password.encode(), name), b"valid", hash(name.encode()))

     def view_all(self, master_password):
          table = PrettyTable()
          table.field_names = ["ID", "Username", "Url", "Password"]
          for i in self.items:
               table.add_row([i,self.items[i].get_username(master_password).decode(), self.items[i].url ,self.items[i].get_password(master_password).decode()])
          print(table)
          print(self._token_table)
          print(self._token_table_reversed)

     @classmethod
     def get_vault(cls, name, master_password):
          try:
               with open(f'{name}.txt', 'rb') as file:
                    vault = pickle.load(file)
                    # Checks that the master password is the same as the one inputted without storing it
                    if aes_encrypt_data(derive_key(master_password.encode(), name), b"valid", hash(name.encode())) == vault.check:
                         return vault
                    else:
                         return False
          # If the file doesn't exist then create vault
          except Exception as e:
               return Vault(name, master_password)

     def get_item(self, id):
          try:
               return self.items[id]
          except Exception as e:
               return False

     def add_item(self, vault_item, master_password):
          # add to dict
          # choose lowest accessible key
          if len(self.removed) == 0:
               id = len(self.items)+1
          else:
               id = self.removed[0]
               del self.removed[0]
          self.items[id] = vault_item
          # updates tokens
          self.tokeniser(vault_item, id, master_password)
          self._save()

     def remove_item(self, id):
          try:
               self.items.pop(id)
               self.removed.append(id)
               self.remove_tokens(id)
               self._save()
          except Exception as e:
               print("error - no valid id")

     def tokeniser(self, vault_item, id, master_password):
          # create partials tokens
          # adds tokens to token table - it is now unsorted
          # all tokens are lowercase
          user = vault_item.get_username(master_password).decode().lower()
          url = vault_item.url.lower()

          for i in [user, url]:
               self.partial_tokens(i, id)
               self.remove_punc_tokens(i, id)

          # sorts token table
          self._token_table = self.merge_sort(self._token_table)
          self._token_table_reversed = self.reverse_table()

     def remove_tokens(self, id):
          for i in self._token_table:
               if i[1] == id:
                    self._token_table.remove(i)

     # is it more efficient to reverse the whole fully sorted list than reverse and order the new elements and add those to the table as that takes 2 merge sorts instead of using once and then O(n) flipping process
     # especially the more complex the systems get for tokens

     def reverse_table(self):
          output = []
          for i in self._token_table[::-1]:
               temp = [i[0][::-1], i[1]]
               output.append(temp)
          return output

     def partial_tokens(self, str, id):
          for i in range(1, len(str)):
               self._token_table.append([str[:i], id])
               self._token_table.append([str[i:], id])
     
     def remove_punc_tokens(self, str, id):
          self._token_table.append([str.translate(str.maketrans('', '', string.punctuation)), id])
     
     #def fuzzy_tokens(self, str, id):
     #     for char in str:


     # maybe instead of doing case sensetivity make all inputs lowercase
     #def all_cases_tokens(self, str, id):

     # can be improved knowing that the first part of the list is already sorted O(nlog(n))
     def merge_sort(self, arr):
          if len(arr) <= 1:
               return arr
          
          mid = len(arr) // 2
          left_half = self.merge_sort(arr[:mid])
          right_half = self.merge_sort(arr[mid:])
          
          return self.merge(left_half, right_half)
     
     def merge(self, l, r):
          sorted_arr = []
          i = j = 0
          
          while i < len(l) and j < len(r):
               if l[i] < r[j]:
                    sorted_arr.append(l[i])
                    i += 1
               else:
                    sorted_arr.append(r[j])
                    j += 1
          
          sorted_arr.extend(l[i:])
          sorted_arr.extend(r[j:])
          
          return sorted_arr

     def _save(self):
          with open(f'{self._name}.txt', 'wb') as file:
               pickle.dump(self, file)
import os
import pickle

from binarysearcharr2d import binary_search_arr2d
from utilities.tokeniser import extract_url_parts
from prettytable import PrettyTable

# from inverseIndex import InverseIndex
from vaultItem import VaultItem

from utilities.encryption import aes_decrypt_data, aes_encrypt_data, hash
from utilities.key import derive_key

class Vault:
     def __init__(self, name, master_password):
          self.name = name
          self.master_password = master_password
          self.items = {}
          self.check = aes_encrypt_data(derive_key(master_password.encode(), name), b"valid", hash(name.encode()))
          self.inverse_index = {}

     def add_to_inverse_index(self, item, index):
          if item in self.inverse_index:
               temp = self.inverse_index[item]
               temp.extend(index)
               self.inverse_index[item] = list(set(temp))
          else:
               self.inverse_index[item] = index

     def remove_from_inverse_index(self, index):
          keys = self.inverse_index.keys()
          to_remove = []
          for item in keys:
               print(item)
               if index in self.inverse_index[item]:
                    if len(self.inverse_index[item]) == 1:
                         to_remove.append(item)
                    self.inverse_index[item].remove(index)
          for item in to_remove:
               del self.inverse_index[item]
               
     def get_items_as_list(self):
          list = []
          count = 0
          for i in self.items:
               count += 1
               list.append((count, self.items[i].url))
          return list

     def get_password(self, url):
          vault_item = self.items[url]
          return vault_item.get_password(self.master_password)
     
     def get_username(self, url):
          vault_item = self.items[url]
          return vault_item.get_username(self.master_password)

     @classmethod
     def get_vault(cls, name, master_password):
          try:
               with open(os.path.join('vault', f'{name}.spam'), 'rb') as file:
                    vault = pickle.load(file)

                    # Checks that the master password is the same as the one inputted without storing it
                    if aes_encrypt_data(derive_key(master_password.encode(), name), b"valid", hash(name.encode())) == vault.check:
                         return vault
                    else:
                         return None
          # If the file doesn't exist then create vault
          except Exception as e:
               return Vault(name, master_password)

     def _get_vault_item(self, url, username, password):
          return VaultItem(self.master_password, url, username, password)

     def get_item(self, url):
          try:
               return self.items[url]
          except Exception as e:
               return False

     def add_item(self, url, username, password):
          vault_item = self._get_vault_item(url, username, password)
          self.items[url] = vault_item
          # updates tokens
          self.build_search(vault_item)
          self._save()
     
     def search(self, query):
          try:
               id_list = self.inverse_index[query]
          except KeyError as e:
               return []
          results = []
          if id_list != None:
               for i in range(len(id_list)):
                    item = self.get_item(id_list[i])
                    results.append((i+1, item.url))
          return results

     def build_search(self, vault_item):
          # tokens = generate_tokens(vault_item.get_username(self.master_password).decode(), vault_item.url)
          tokens = extract_url_parts(vault_item.url, vault_item.url)
          for i in tokens:
               self.add_to_inverse_index(i[0], i[1])

     def remove_item(self, url):
          try:
               print("fails here")
               self.items.pop(url)
               print("working 1")
               self.remove_from_inverse_index(url)
               print("working 2")
               self._save()
               print("working 3")
          except Exception as e:
               print("error - invalid item")

     def _save(self):
          folder = 'vault'
          if not os.path.exists(folder):
               os.makedirs(folder)
          with open(os.path.join(folder, f'{self.name}.spam'), 'wb') as file:
               pickle.dump(self, file)

     # def __getstate__(self):
     #      """ Convert inverse_index into a 2D list before pickling """
     #      state = self.__dict__.copy()
     #      state["inverse_index"] = self.inverse_index.save()  # Store as a serializable list
     #      return state

     # def __setstate__(self, state):
     #      """ Restore inverse_index from a 2D list after unpickling """
     #      self.__dict__.update(state)
     #      self.inverse_index = InverseIndex(state.get("inverse_index", []))  # Reconstruct it properly

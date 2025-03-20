import os
import pickle

from binarysearcharr2d import binary_search_arr2d
from utilities.tokeniser import generate_tokens
from prettytable import PrettyTable

from inverseIndex import InverseIndex
from vaultItem import VaultItem

from utilities.encryption import aes_decrypt_data, aes_encrypt_data, hash
from utilities.key import derive_key

class Vault:
     def __init__(self, name, master_password):
          self.name = name
          self.master_password = master_password
          self.items = {}
          self.check = aes_encrypt_data(derive_key(master_password.encode(), name), b"valid", hash(name.encode()))
          self.inverse_index = InverseIndex()

     def get_items_as_list(self):
          list = []
          for i in self.items:
               list.append((self.items[i].id, self.items[i].url))
          return list

     def get_password(self, url):
          vault_item = self.items[url]
          return vault_item.get_password(self.master_password)
     
     def get_username(self, url):
          vault_item = self.items[url]
          return vault_item.get_username(self.master_password)

     def view_all(self):
          table = PrettyTable()
          table.field_names = ["ID", "Username", "Url", "Password"]
          for i in self.items:
               table.add_row([i,self.items[i].get_username(self.master_password).decode(), self.items[i].url ,self.items[i].get_password(master_password).decode()])
          print(table)

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

     def get_item(self, id):
          print(self.items)
          print(id)
          try:
               return self.items[id]
          except Exception as e:
               return False

     def add_item(self, url, username, password):
          vault_item = self._get_vault_item(url, username, password)
          self.items[url] = vault_item
          # updates tokens
          self.build_search(vault_item)
          self._save()
     
     def search(self, query):
          id_list = self.inverse_index.search(query)
          print('tt')
          print(id_list)
          results = []
          if id_list != None:
               for i in range(len(id_list)):
                    item = self.get_item(id_list[i])
                    results.append((item.get_username(self.master_password), item.url, item.get_password(self.master_password)))
          return results

     def build_search(self, vault_item):
          tokens = generate_tokens(vault_item.get_username(self.master_password).decode(), vault_item.url)
          tokens.extend(generate_tokens(vault_item.url, vault_item.url))
          print(tokens)
          for i in tokens:
               self.inverse_index.add(i[0], i[1])

     def remove_item(self, url):
          try:
               self.items.pop(url)
               self.inverse_index.delete(url)
               self._save()
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

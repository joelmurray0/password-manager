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
          self.items = {}
          self.removed = []
          self._token_table = []
          self.check = aes_encrypt_data(derive_key(master_password.encode(), name), b"valid", hash(name.encode()))
          self.inverse_index = InverseIndex()

     def view_all(self, master_password):
          table = PrettyTable()
          table.field_names = ["ID", "Username", "Url", "Password"]
          for i in self.items:
               table.add_row([i,self.items[i].get_username(master_password).decode(), self.items[i].url ,self.items[i].get_password(master_password).decode()])
          print(table)

     @classmethod
     def get_vault(cls, name, master_password):
          try:
               with open(os.path.join('vault', f'{name}.txt'), 'rb') as file:
                    vault = pickle.load(file)
                    # Checks that the master password is the same as the one inputted without storing it
                    if aes_encrypt_data(derive_key(master_password.encode(), name), b"valid", hash(name.encode())) == vault.check:
                         return vault
                    else:
                         return None
          # If the file doesn't exist then create vault
          except Exception as e:
               return Vault(name, master_password)

     @classmethod
     def login(cls, name, master_password):
          try:
               with open(os.path.join('vault', f'{name}.txt'), 'rb') as file:
                    vault = pickle.load(file)
                    # Checks that the master password is the same as the one inputted without storing it
                    if aes_encrypt_data(derive_key(master_password.encode(), name), b"valid", hash(name.encode())) == vault.check:
                         return True
                    else:
                         return False
          # If the file doesn't exist then create vault
          except Exception as e:
               return False

     def get_item(self, vault_item):
          try:
               return self.items[vault_item.id]
          except Exception as e:
               return False

     def add_item(self, vault_item, master_password):
          # add to dict
          # choose lowest accessible key
          while vault_item.id in self.items.keys():
               vault_item.id = os.urandom(16)
          self.items[vault_item.id] = vault_item
          # updates tokens
          self.build_search(vault_item, master_password)
          self._save()
     
     def build_search(self, vault_item, master_password):
          tokens = generate_tokens(vault_item.get_username(master_password).decode(), 1)
          tokens.extend(generate_tokens(vault_item.url, 1))
          for i in tokens:
               self.inverse_index.add(i[0], i[1])
          self.inverse_index.display()

     def remove_item(self, vault_item):
          try:
               self.items.pop(vault_item.id)
               self.inverse_index.delete(vault_item.id)
               self._save()
          except Exception as e:
               print("error - invalid item")

     def __getstate__(self):
          state = self.__dict__.copy()
          state["inverse_index"] = None  # Remove before pickling
          return state

     def __setstate__(self, state):
          self.__dict__.update(state)
          self.inverse_index = InverseIndex()  # Restore after unpickling

     def _save(self):
          folder = 'vault'
          if not os.path.exists(folder):
               os.makedirs(folder)
          
          with open(os.path.join(folder, f'{self.name}.txt'), 'wb') as file:
               pickle.dump(self, file)

     def search(self): # write search for inverse index
          pass
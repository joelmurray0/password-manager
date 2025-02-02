import pickle
from encryption import aes_decrypt_data, aes_encrypt_data, hash
from key import derive_key
from vaultItem import VaultItem
import os

class Vault:
     def __init__(self, name):
          self._name = name
          self.items = {}

     @classmethod
     def get_vault(cls, name):
          try:
               with open(f'{name}.txt', 'rb') as file:
                    return pickle.load(file)
          except Exception as e:
               return Vault(name)

     def get_item(self, url):
          try:
               return self.items[url]
          except Exception as e:
               return False

     def add_item(self, vault_item):
          # add to dict
          self.items[vault_item.url] = vault_item
          self._save()

     def remove_item(self, url):
          try:
               del self.items[url]
               self._save()
          except Exception as e:
               print("error - no valid url")

     def _save(self):
          with open(f'{self._name}.txt', 'wb') as file:
               pickle.dump(self, file)

# new idea: master password is made into key which decrypts the key in each password object - which decodes the password
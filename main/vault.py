from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import pickle
from vaultItem import VaultItem
from key import derive_key
from encryption import aes_decrypt_data, aes_encrypt_data, hash
import base64

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

     def add_item(self, vault_item):
          # add to dict
          self.items[vault_item.url] = vault_item
          self._save()

     def remove_item(self, vault_item):
          del self.items[vault_item.url]
          self._save()

     def _save(self):
          with open(f'{self._name}.txt', 'wb') as file:
               pickle.dump(self, file)

vault = Vault.get_vault("joel")

# new idea: master password is made into key which decrypts the key in each password object - which decodes the password
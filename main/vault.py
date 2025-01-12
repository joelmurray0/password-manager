from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import json
from .vaultItem import VaultItem
from .key import Key
from encryption import Encryption

class Vault:
     def __init__(self, key):
          self._key = key
          self.items = {}
          self.encryption = Encryption()
          self.hash_map = []

     def add_item(self, vault_item):
          # check for actual vault item
          if not isinstance(vault_item, VaultItem):
               raise TypeError
          # add to dict
          self.items[vault_item._url] = vault_item
          self.add_to_hash_map(vault_item)

     def remove_item(self, vault_item):
          if isinstance(vault_item, VaultItem):
               self.items[vault_item.url] = None
     
     def add_to_hash_map(self):
          #hash_value 
          pass

     def write_vault_item_to_file(self, vault_item, password):
          vault_item.lock_vaultItem(password)
          with open(f'{self._key.name}.txt', 'w') as file:
               items = vault_item.reveal_items()
               file.write(f'{items[0]}\n{items[1]}\n{items[2]}\n{items[3]}') # writes url usr password and key in that order with usr and password encrypted

     def write_all_vault_items_to_file(self, password):
          counter = 1
          for vault_item in self.items.values():
               counter += 1
               vault_item.lock_vaultItem(password)
               hash_map.append([self.encryption.hash(vault_item.url), counter])

          with open(f'{self._key.name}.txt', 'w') as file:
               # write hash map line

               items = vault_item.reveal_items()
               
               file.write(f'{items[0]}\n{items[1]}\n{items[2]}\n{items[3]}') # writes url usr password and key in that order with usr and password encrypted

     def write_hash_map(self):
          for 

     def items_json(self):
          with open('data.json', 'w') as file:
               json.dump(self.items, file)
     
     def write_to_vault(self):
          data = ''
          for i in vault.items.values():
               data += json.dumps(i.__dict__)

          ciphertext = self.encrypt_data(data.encode())
          with open(f"{self._key.vault_name}.txt", "wb") as f:
               f.write(ciphertext)
          
     def read_from_vault(self):
          with open(f"{self._key.vault_name}.txt", "rb") as f:
               ciphertext = f.read()
               print(ciphertext)
               print()
               return self.decrypt_data(ciphertext)

key = Key('keira', 'joel')
vault = Vault(key)
#key = vault.derive_key('keira')
###ciphertext = vault.encrypt_data(key, b"welcome to the password manager")
#print(ciphertext)

#plaintext = vault.decrypt_data(key, ciphertext)
#print(plaintext)
#print(json.dumps(vault.items))


item = VaultItem("google.com", "joel", "password", "keira")
item2 = VaultItem("bing.com", "jim", "supersecret", "cat")

vault.add_item(item)
vault.add_item(item2)
#print(vault.items)
vault.write_to_vault()
print()
print(vault.items)
print()
print(vault.read_from_vault())

# Write object to a text file as JSON



#with open('data.txt', 'r') as file:
#    loaded_data = json.load(file)

#vault.add_item(item)
#vault.items_json()




# new idea: master password is made into key which decrypts the key in each password object - which decodes the password
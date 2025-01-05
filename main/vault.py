from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import json
from vaultItem import VaultItem
from key import Key

class Vault:
     def __init__(self, key):
          self._key = key
          self.items = {}

     def add_item(self, vault_item):
          # check for actual vault item
          if not isinstance(vault_item, VaultItem):
               raise TypeError
          # add to dict
          self.items[vault_item._url] = vault_item


     def remove_item(self, vault_item):
          if isinstance(vault_item, VaultItem):
               self.items[vault_item._url] = None

     def items_json(self):
          with open('data.json', 'w') as file:
               json.dump(self.items, file)

     def encrypt_data(self, data):
          # Pad the data to ensure it is a multiple of AES's block size (128 bits / 16 bytes)
          padder = padding.PKCS7(algorithms.AES.block_size).padder()
          padded_data = padder.update(data) + padder.finalize()

          # Generate a random IV (Initialization Vector)
          iv = os.urandom(16)

          # Create a Cipher object using AES and CBC mode
          cipher = Cipher(algorithms.AES(self._key._key), modes.CBC(iv), backend=default_backend())
          encryptor = cipher.encryptor()

          # Encrypt the padded data
          encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

          # Return the IV concatenated with the encrypted data
          return iv + encrypted_data

     def decrypt_data(self, ciphertext):
          # Extract the IV from the beginning of the ciphertext
          iv = ciphertext[:16]
          actual_ciphertext = ciphertext[16:]

          # Create a Cipher object using AES and CBC mode
          cipher = Cipher(algorithms.AES(self._key._key), modes.CBC(iv), backend=default_backend())
          decryptor = cipher.decryptor()

          # Decrypt the ciphertext
          padded_data = decryptor.update(actual_ciphertext) + decryptor.finalize()

          # Unpad the decrypted data
          unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
          data = unpadder.update(padded_data) + unpadder.finalize()

          return data
     
     def write_to_file(self):
          data = ''
          for i in vault.items.values():
               data += json.dumps(i.__dict__)
          
          print(data)
          ciphertext = self.encrypt_data(data.encode())
          with open(f"{self._key.vault_name}.txt", "wb") as f:
               f.write(ciphertext)
          
     def read_from_file(self):
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
vault.write_to_file()
print()
print(vault.items)
print()
print(vault.read_from_file())

# Write object to a text file as JSON



#with open('data.txt', 'r') as file:
#    loaded_data = json.load(file)

#vault.add_item(item)
#vault.items_json()
import hashlib
import os

class Encryption:
     def __init__(self, master_password, hash):
          self.hash = hash
          self._encryption_key = self.perform_hash(master_password)
     
     def get_encryption_key(self):
          return self._encryption_key

     def perform_hash(self, data):
          h = hashlib.new(self.hash)
          h.update(data.encode())
          return h.digest()
     
     def encrypt_bytes(self, plaintext):
          if not isinstance(plaintext, bytes):
               plaintext = plaintext.encode()
          # xors plaintext with hashed master password
          return bytes(a ^ b for a, b in zip(plaintext, self.get_encryption_key()))
     
     def decrypt_bytes(self, ciphertext):
          if not isinstance(ciphertext, bytes):
               ciphertext = ciphertext.encode()
          return bytes(b ^ a for a, b in zip(ciphertext, self.get_encryption_key()))
          
     def encrypt_to_file(self, plaintext, file):
          with open(file, "ab") as vault_file:
               vault_file.write(self.encrypt_bytes(plaintext))
     
     def encrypt_file(self, file):
          with open(file, "r") as vault_file:
               contents = vault_file.read()
               self.encrypt_to_file(contents, file)

     def decrypt_file(self, file):
          with open(file, "r") as vault_file:
               contents = vault_file.read()
          with open(file, "wb") as vault_file:
               vault_file.write(self.decrypt_bytes(contents))


vault = Encryption("password", "sha3_256")

plaintext = "abcd"


vault.encrypt_to_file(plaintext, os.path.join("proto", "vault.txt"))
vault.decrypt_file(os.path.join("proto", "vault.txt"))

ciphertext = vault.encrypt_bytes(plaintext)

print(plaintext)
print(ciphertext)
print(vault.decrypt_bytes(ciphertext))
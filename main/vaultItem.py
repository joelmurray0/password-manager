from utilities.encryption import aes_decrypt_data, aes_encrypt_data, hash
from utilities.key import derive_key
import os
import base64

class VaultItem:
     def __init__(self, master_password, url, username, password):
          self.url = url
          self._put(master_password, url, username, password)

     def _put(self, master_password, url, username, password):
          # plain key is derived from the website, master password, and account specific key
          # encrypt username and password
          iv = hash(self.url.encode())
          self._key = os.urandom(16)

          self._username = base64.b64encode(aes_encrypt_data(derive_key(self._key, url), username.encode(), iv))
          self._password = base64.b64encode(aes_encrypt_data(derive_key(self._key, url), password.encode(), iv))
          self._key = base64.b64encode(aes_encrypt_data(derive_key(master_password.encode(), url), self._key, iv))

     def get_username(self, master_password):
          key = aes_decrypt_data(derive_key(master_password.encode(), self.url), self.decode_key())

          # decrypt username
          return aes_decrypt_data(derive_key(key, self.url), base64.b64decode(self._username))

     def get_password(self, master_password):
          key = aes_decrypt_data(derive_key(master_password.encode(), self.url), self.decode_key())

          # decrypt password
          return aes_decrypt_data(derive_key(key, self.url), base64.b64decode(self._password))
     
     def decode_key(self):
          return base64.b64decode(self._key)
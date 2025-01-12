from encryption import Encryption
from key import Key

class VaultItem:
     def __init__(self, url, username, password, key):
          self.url = url
          self._usr = username
          self._password = password
          self._key = key
          self.encryption = Encryption()
          self.combin_key = Key("unlock")
          self.is_locked = False

     def reveal_items(self):
          return [self.url, self._usr.decode('utf-8', errors='ignore'), self._password.decode('utf-8', errors='ignore'), self._key]

     def lock_vaultItem(self, master_password):
          # plain key is derived from the website, master password, and account specific key
          # encrypt username and password
          
          iv = self.encryption.hash(self.url.encode())
          self._usr = self.encryption.aes_encrypt_data(self.combin_key.derive_key(master_password + self._key), self._usr.encode(), iv)
          self._password = self.encryption.aes_encrypt_data(self.combin_key.derive_key(master_password + self._key), self._password.encode(), iv)
          self.is_locked = True

     def unlock_vaultItem(self, master_password):
          # encrypt username and password
          self._usr = self.encryption.aes_decrypt_data(self.combin_key.derive_key(master_password + self._key), self._usr)
          self._password = self.encryption.aes_decrypt_data(self.combin_key.derive_key(master_password + self._key), self._password)
          self.is_locked = False



# pass1 = VaultItem('google.com', 'plonker', 'secret', 'pass')
# pass2 = VaultItem("twitter.com", "planks", "shush", "please")

# pass1.lock_vaultItem("master")
# print(pass1.reveal_items())
# pass1.unlock_vaultItem("master")
# print(pass1.reveal_items())
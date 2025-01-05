class VaultItem:
     def __init__(self, url, username, password, key="init"):
          self._url = url
          self._usr = username
          self._password = password
          self._key = key

     def encrypt_password(self):
          self._password = self.encryption.encrypt_data(self._key, self._password)
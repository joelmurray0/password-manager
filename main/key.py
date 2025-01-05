from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

class Key:
     def __init__(self, password, vault_name):
          self.vault_name = vault_name
          self._key = self.derive_key(password, vault_name)

     def derive_key(self, password, vault_name, iterations=600000):
          # Derive a 256-bit AES key using PBKDF2 with SHA-256
          kdf = PBKDF2HMAC(
               algorithm=hashes.SHA256(),
               length=32,  # AES-256 requires a 32-byte key
               salt=vault_name.encode(),
               iterations=iterations,
               backend=default_backend()
          )
          return kdf.derive(password.encode())
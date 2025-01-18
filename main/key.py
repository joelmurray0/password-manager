from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def derive_key(lock, salt, iterations=600000):
     # Derive a 256-bit AES key using PBKDF2 with SHA-256
     kdf = PBKDF2HMAC(
          algorithm=hashes.SHA256(),
          length=32,  # AES-256 requires a 32-byte key
          salt=salt.encode(),
          iterations=iterations,
          backend=default_backend()
     )
     return kdf.derive(lock)
import os
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def aes_encrypt_data(key, data, iv = os.urandom(16)):
     # Pad the data to ensure it is a multiple of AES's block size (128 bits / 16 bytes)
     padder = padding.PKCS7(algorithms.AES.block_size).padder()
     padded_data = padder.update(data) + padder.finalize()
     
     # Create a Cipher object using AES and CBC mode
     cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
     encryptor = cipher.encryptor()

     # Encrypt the padded data
     encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

     # Return the IV concatenated with the encrypted data
     return iv + encrypted_data

def aes_decrypt_data(key, ciphertext):
     # Extract the IV from the beginning of the ciphertext
     iv = ciphertext[:16]
     actual_ciphertext = ciphertext[16:]

     # Create a Cipher object using AES and CBC mode
     cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
     decryptor = cipher.decryptor()

     # Decrypt the ciphertext
     padded_data = decryptor.update(actual_ciphertext) + decryptor.finalize()

     # Unpad the decrypted data
     unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
     data = unpadder.update(padded_data) + unpadder.finalize()

     return data

def hash(data):
     digest = hashes.Hash(hashes.SHA256())
     digest.update(data)

     # Compute the full hash and truncate it to 16 bytes
     full_hash = digest.finalize()
     return full_hash[:16]
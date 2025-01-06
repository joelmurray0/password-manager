import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class Encryption:
     def aes_encrypt_data(self, key, data, iv = os.urandom(16)):
          # Pad the data to ensure it is a multiple of AES's block size (128 bits / 16 bytes)
          padder = padding.PKCS7(algorithms.AES.block_size).padder()
          padded_data = padder.update(data) + padder.finalize()

          # Generate a random IV (Initialization Vector)
          

          # Create a Cipher object using AES and CBC mode
          cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
          encryptor = cipher.encryptor()

          # Encrypt the padded data
          encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

          # Return the IV concatenated with the encrypted data
          return iv + encrypted_data

     def aes_decrypt_data(self, key, ciphertext):
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
     
cipher = Encryption()
print(cipher.aes_encrypt_data(b"00000000000000000000000000000000", b"6a84867cd77e12ad07ea1be895c53fa3", b"0000000000000000"))
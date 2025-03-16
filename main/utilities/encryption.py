import os
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def aes_encrypt_data(key, data, iv = os.urandom(16)):
    # Generate a 16-byte IV
    padder = padding.PKCS7(128).padder()  # AES block size is 128 bits (16 bytes)
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return iv + encrypted_data  # Prepend IV to ciphertext

def aes_decrypt_data(key, ciphertext):
    iv = ciphertext[:16]  # Extract IV
    actual_ciphertext = ciphertext[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(actual_ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    return data

def hash(data):
    digest = hashes.Hash(hashes.SHA256())  # Use SHA-256
    digest.update(data)
    return digest.finalize()[:16]  # Return full 16-byte key










# from crypto.Cipher import AES
# from crypto.Util.Padding import pad, unpad
# from crypto.Random import get_random_bytes
# import base64

# def aes_encrypt_data(key: bytes, plaintext: str) -> str:
#     """
#     Encrypts the plaintext using AES-256 in CBC mode with PKCS7 padding.
    
#     Args:
#         plaintext (str): The text to be encrypted.
#         key (bytes): A 32-byte encryption key for AES-256.
    
#     Returns:
#         str: The base64-encoded string containing the IV and ciphertext.
#     """
#     # Generate a random initialization vector (IV)
#     iv = get_random_bytes(AES.block_size)  # AES.block_size is 16 bytes
#     cipher = AES.new(key, AES.MODE_CBC, iv)
    
#     # Pad the plaintext to be a multiple of the block size and encrypt it
#     padded_data = pad(plaintext.encode('utf-8'), AES.block_size)
#     ciphertext = cipher.encrypt(padded_data)
    
#     # Prepend the IV to the ciphertext. The IV is needed for decryption.
#     encrypted_data = iv + ciphertext
    
#     # Return the result as a base64-encoded string for easy storage/transmission
#     return base64.b64encode(encrypted_data).decode('utf-8')

# def aes_decrypt_data(key: bytes, ciphertext_b64: str) -> str:
#     """
#     Decrypts the base64-encoded ciphertext using AES-256 in CBC mode with PKCS7 padding.
    
#     Args:
#         ciphertext_b64 (str): The base64 encoded ciphertext (with the IV prepended).
#         key (bytes): A 32-byte decryption key for AES-256.
    
#     Returns:
#         str: The original plaintext.
#     """
#     # Decode the base64 encoded data to get back the raw bytes
#     encrypted_data = base64.b64decode(ciphertext_b64)
    
#     # The first 16 bytes are the IV
#     iv = encrypted_data[:AES.block_size]
#     ciphertext = encrypted_data[AES.block_size:]
    
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     padded_data = cipher.decrypt(ciphertext)
    
#     # Remove the padding to get back the original plaintext
#     plaintext = unpad(padded_data, AES.block_size)
#     return plaintext.decode('utf-8')

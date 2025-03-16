from main.utilities.encryption import aes_decrypt_data, aes_encrypt_data, hash

def test_aes_encrypt_data():
     ciphertext = aes_encrypt_data(b"0000000000000000", b"data")

     assert isinstance(ciphertext, bytes)
     assert ciphertext != b"data"
     assert len(ciphertext) != 0

def test_aes_decrypt_data():
     ciphertext = aes_encrypt_data(b"0000000000000000", b"data")

     plaintext = aes_decrypt_data(b"0000000000000000", ciphertext)

     assert plaintext == b"data"

def test_hash():
     hash_result = hash(b"data")

     assert isinstance(hash_result, bytes)
     assert hash_result != b"data"
     assert len(hash_result) == 16
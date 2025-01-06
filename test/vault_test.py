import pytest
from main.vault import Vault
from main.key import Key

def test_create_vault():
     vault = Vault('name')

     assert vault._key == 'name'
     assert vault.items == {}
     assert isinstance(vault, Vault)

#def test_write_to_vault()

def test_encrypt():
     key = Key("key", "name")
     vault = Vault(key)
     plaintext = b"sample"
     ciphertext = vault.encrypt_data(plaintext)
     assert ciphertext != plaintext 
     assert vault.decrypt_data(ciphertext) == plaintext
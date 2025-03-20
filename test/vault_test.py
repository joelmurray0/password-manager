from main.vault import Vault
from main.vaultItem import VaultItem
import os
import pytest


@pytest.fixture(autouse=True)
def setup():
     file_path = os.path.join("vault", "vault.txt")

     # Check if the file exists before deleting
     if os.path.exists(file_path):
          os.remove(file_path)
          

def test_create_vault():
     vault = Vault.get_vault(name='name', master_password='pass')

     assert vault.name == 'name'
     assert vault.items == {}
     assert isinstance(vault, Vault)

def test_add_item():
     # Arrange
     vault = Vault.get_vault(name="vault", master_password='master_password')
     # Act
     vault.add_item("url", "username", "password")

     assert vault.items["url"].url == "url"
     assert vault.get_username("url") == b"username"
     assert vault.get_password("url")  == b"password"

# def test_get_item():
#      vault = Vault.get_vault(name="vault", master_password='master_password')

#      vault.add_item("url", "username", "password")

#      assert vault.get_item("url").url == "url

def test_remove_item(): # every other test fails
     # Arrange
     vault = Vault.get_vault(name="vault", master_password="master_password")
     
     vault.add_item("url", "username", "password")

     # Act
     vault.remove_item("url")

     # Assert
     assert vault.get_item("url") not in vault.items

def test__save(): # inverse index is the problem
     vault = Vault.get_vault(name="vault", master_password="master_password")
     vault.add_item("url", "username", "password")
     vault._save()

     with open(os.path.join('vault', "vault.spam"), "rb") as file:
          content = file.read()
          assert isinstance(content, bytes)
          assert len(content) != 0

def test_get_vault_can_also_load_pre_existing_vaults():
     vault = Vault.get_vault(name="vault", master_password="master_password")  
     
     vault.add_item("url", "username", "password")
     vault._save()

     with open(os.path.join('vault', "vault.txt"), "rb") as file:
          content = file.read()
          assert isinstance(content, bytes)
          assert len(content) != 0
     vault = Vault.get_vault(name="vault", master_password="master_password")

     assert list(vault.items.keys())[-1] == id # last element as previous tests take up other ids that aren't removed

def test_build_search():
     vault = Vault.get_vault(name="vault", master_password="master_password")
     

     vault.build_search(vault_item)

def test_get_item_with_id():
     vault = Vault.get_vault(name="vault", master_password="master_password")
     

     vault.add_item("url", "username", "password")

     new_vault_item = vault.get_item(vault_item.id)

     assert vault_item.url == new_vault_item.url
     assert vault_item.get_password("master_password") == new_vault_item.get_password("master_password")
     assert vault_item.get_username("master_password") == new_vault_item.get_username("master_password")
     assert vault_item.id == new_vault_item.id

def test_inverse_index_exists_after_saving_and_loading():
     vault = Vault.get_vault(name="vault", master_password="master_password")
     

     vault.add_item("url", "username", "password")

     vault.inverse_index.display()
     print(vault.inverse_index.head)
     vault._save()

     new_vault = Vault.get_vault(name="vault", master_password="master_password")
     #assert vault.inverse_index.display() == new_vault.inverse_index.display()

     # new_vault.inverse_index.display()
     # print(new_vault.inverse_index.head)
     print(new_vault.inverse_index.search("vsername"))#
     # print(new_vault.inverse_index.head)
     #print(b's\x10\x80\x84\xfcW/PgUe\xa7\x14aK\xae')

     assert vault.inverse_index is new_vault.inverse_index
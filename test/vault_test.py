from main.vault import Vault
from main.vaultItem import VaultItem
import os

def test_create_vault():
     vault = Vault.get_vault(name='name', master_password='pass')

     assert vault.name == 'name'
     assert vault.items == {}
     assert isinstance(vault, Vault)

def test_add_item():
     # Arrange
     vault = Vault.get_vault(name="vault", master_password='master_password')
     vault_item = VaultItem("master_password", "url", "username", "password")
     id = vault_item.id
     # Act
     vault.add_item(vault_item, 'master_password')

     # Assert
     assert id in vault.items
     assert vault.items[id] is vault_item

def test_remove_item():
     # Arrange
     vault = Vault.get_vault(name="vault", master_password="master_password")
     vault_item = VaultItem("master_password", "url", "username", "password")
     vault.add_item(vault_item, "master_password")

     # Act
     vault.remove_item(vault_item)

     # Assert
     assert vault_item.id not in vault.items

def test__save():
     vault = Vault.get_vault(name="vault", master_password="master_password")
     vault_item = VaultItem("master_password", "url", "username", "password")
     id = vault_item.id
     vault.add_item(vault_item, "master_password")
     vault._save()

     with open(os.path.join('vault', "vault.txt"), "rb") as file:
          content = file.read()
          assert isinstance(content, bytes)
          assert len(content) != 0
     vault = Vault.get_vault(name="vault", master_password="master_password")

     assert list(vault.items.keys())[-1] == id # last element as previous tests take up other ids that aren't removed

def test_build_search():
     vault = Vault.get_vault(name="vault", master_password="master_password")
     vault_item = VaultItem("master_password", "url", "username", "password")

     vault.build_search(vault_item, "master_password")
     
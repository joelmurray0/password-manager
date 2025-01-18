from main.vault import Vault
from main.vaultItem import VaultItem

def test_create_vault():
     vault = Vault.get_vault('name')

     assert vault._name == 'name'
     assert vault.items == {}
     assert isinstance(vault, Vault)

def test_add_item():
     # Arrange
     vault = Vault.get_vault(name="vault")
     vault_item = VaultItem("master_password", "url", "username", "password")

     # Act
     vault.add_item(vault_item)

     # Assert
     assert "url" in vault.items
     assert vault.items["url"] is vault_item

def test_remove_item():
     # Arrange
     vault = Vault.get_vault(name="vault")
     vault_item = VaultItem("master_password", "url", "username", "password")

     # Act
     vault.remove_item(vault_item)

     # Assert
     assert "url" not in vault.items

def test__save():
     vault = Vault.get_vault(name="vault")

     vault._save()

     with open("vault.txt", "rb") as file:
          content = file.read()
          assert isinstance(content, bytes)
          assert len(content) != 0
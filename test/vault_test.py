import pytest
from main.vault import Vault
from main.vaultItem import VaultItem


def test_create_vault():
     vault = Vault('name')

     assert vault.name == 'name'
     assert vault.items == {}
     assert isinstance(vault, Vault)

def test_add_item():
     vault = Vault('name')
     vault_item = VaultItem()

     vault.add_item("item")
     assert vault.items == {}

     vault.add_item(vault_item)
     assert vault.items == {vault_item._key: vault_item}

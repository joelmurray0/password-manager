from main.vaultItem import VaultItem

def test__put():
     vault_item = VaultItem("master_password", "url.com", "username", "password")
     
     assert vault_item._username != "username"
     assert vault_item._password != "password"
     assert isinstance(vault_item._key, bytes) and len(vault_item._key) != 0

def test_get_username():
     vault_item = VaultItem("master_password", "url.com", "username", "password")

     assert vault_item.get_username("master_password") == b"username"

def test_get_password():
     vault_item = VaultItem("master_password", "url.com", "username", "password")

     assert vault_item.get_password("master_password") == b"password"
import os
from vaultItem import VaultItem
from encryption import Encryption
from key import Key
from vault import Vault

while __name__ == "__main__":
     encryption = Encryption()
     master_key = Key("joel")
     vault = Vault(master_key)
     # object of a vault - add remove edit show functions
     # dont care about input validation for this as not problem in finished code
     master_pass_hash = master_key.derive_key(input("Enter your master password"))
     func = int(input("1. Add \n2. Return \n3. Delete \n4. Edit \n5. Exit"))
     if func == 1:
          usr = input("please enter username")
          password = input("please enter password")
          url = input("what is the url of the website this account is for?")
          item = VaultItem(url, usr, password, os.urandom(16))
          vault.add_item(item)
     elif func == 2:
          url = input("what is the url of the website this account is for?")
     elif func == 3:
          url = input("what is the url of the website this account is for?")
     elif func == 4:
          url = input("what is the url of the website this account is for?")
     elif func == 5:
          # shut down methods
          # write_all_to_file() --> lock all items --> write to txt file 

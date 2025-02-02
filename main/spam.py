# import os
# from vaultItem import VaultItem
# from encryption import Encryption
# from key import Key
# from vault import Vault

# while __name__ == "__main__":
#      encryption = Encryption()
#      master_key = Key("joel")
#      vault = Vault(master_key)
#      # object of a vault - add remove edit show functions
#      # dont care about input validation for this as not problem in finished code
#      master_pass_hash = master_key.derive_key(input("Enter your master password"))
#      func = int(input("1. Add \n2. Return \n3. Delete \n4. Edit \n5. Exit"))
#      if func == 1:
#           usr = input("please enter username")
#           password = input("please enter password")
#           url = input("what is the url of the website this account is for?")
#           item = VaultItem(url, usr, password, os.urandom(16))
#           vault.add_item(item)
#      elif func == 2:
#           url = input("what is the url of the website this account is for?")
#      elif func == 3:
#           url = input("what is the url of the website this account is for?")
#      elif func == 4:
#           url = input("what is the url of the website this account is for?")
#      elif func == 5:
#           # shut down methods
#           # write_all_to_file() --> lock all items --> write to txt file 


import argparse
from vault import Vault
from vaultItem import VaultItem

def greet(name, uppercase):
     message = f"Hello, {name}!"
     if uppercase:
          message = message.upper()
     print(message)

def create_vault(name):
     return Vault.get_vault(name)

def add_to_vault(name, username, password, url, master_password):
     vault = create_vault(name)
     vault_item = VaultItem(master_password, url, username, password)
     vault.add_item(vault_item)

def remove_from_vault(name, url):
     vault = create_vault(name)
     vault.remove_item(url)

def view_from_vault(name, url, master_password):
     vault = create_vault(name)
     item = vault.get_item(url)
     try:
          print(item.get_username(master_password).decode())
          print(item.get_password(master_password).decode())
     except Exception:
          print("Invalid url")


if __name__ == "__main__":
     parser = argparse.ArgumentParser(description="Password Manager CLI")
     # subparsers = parser.add_subparsers(dest="command")

     # Add password command
     # paser = subparsers.paser("add", help="Add a new account and password")
     parser.add_argument("--create", help="Creates a vault given a username.")
     #parser.add_argument("--login", help="logs in to a vault given a username and password.")
     parser.add_argument("--add", nargs=5, help="adds a password given the vault details")
     parser.add_argument("--remove", nargs=2, help="removes a password given the website and username.")
     parser.add_argument("--view", nargs=3, help="view a password given the vault, website and master password.")

     args = parser.parse_args()
     if args.create:
          vault = create_vault(args.create)
     elif args.add:
          add_to_vault(args.add[0], args.add[1], args.add[2], args.add[3], args.add[4])
     elif args.remove:
          remove_from_vault(args.remove[0], args.remove[1])
     elif args.view:
          view_from_vault(args.view[0], args.view[1], args.view[2])
     else:
          parser.print_help()

     # never store master password



# spam --create myvault
#  -- check already exist
# -- tell user created
# -- wroye out file

# spam --add myvault --url google,com --password cooking
# name = input("Enter your new MP: ")
#   -- fail is vault file not ecists
#   -- add vaoult item + write FileNotFoundError
#   -- tell user added itel

# spam --get myvault --url google.com
# name = input("Enter your new MP: ")
#   -- fail is vault file not ecists
#   -- print unencyrypetydf bits to user



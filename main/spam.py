import argparse
from vault import Vault
from vaultItem import VaultItem
from utilities.generatepassword import make_password
from bloomfilter import BloomFilter

def add_to_vault(vault, username, password, url, master_password, password_bloom_filter=BloomFilter.load("password_bloom_filter.pkl")):
     if not password_bloom_filter.__contains__(password):
          vault_item = VaultItem(master_password, url, username, password)
          vault.add_item(vault_item, master_password)
     else:
          print("error - password too weak")

def remove_from_vault(vault, query):
     options = vault.search(query)
     for i in options:
          print(i.url)
     choice = int(input("Select a choice from the presented ones by the order they appear: "))
     print(options[choice-1])
     vault.remove_item(options[choice-1])

def view_from_vault(vault, query, master_password):
     item = vault.get_item(vault.search(query)[0]) # takes an item found in the search as most likely choice
     try:
          print(item.get_username(master_password).decode())
          print(item.get_password(master_password).decode())
     except Exception:
          print("Invalid url")

if __name__ == "__main__":
     parser = argparse.ArgumentParser(description="Password Manager CLI")

     # Defines arguments that can be used with the CLI along with help descriptors
     parser.add_argument("--create", nargs=2, help="Creates a vault given the vault name and master password. -- <name> <password>")
     parser.add_argument("--add", nargs=5, help="adds a password given the vault details -- <name> <master password> <username> <password> <url>")
     parser.add_argument("--remove", nargs=3, help="removes a password given the website and username. -- <name> <master password> <url>")
     parser.add_argument("--view", nargs=3, help="view a password given the vault name, password and website. -- <name> <master password> <query>")
     parser.add_argument("--add_generated", nargs=4, help="adds a generated password given the vault details -- <name> <master password> <username> <url>")
     parser.add_argument("--list", nargs=2, help="Creates a vault given the vault name and master password. -- <name> <password>")
     parser.add_argument("--search", nargs=3, help="show possible passwords given vault name, password and search query")
     parser.add_argument("--check_strength", nargs=4, help="checks strength of password given the vault details -- <name> <master password> <query>")

     args = parser.parse_args()
     if args.create:
          # Code to check the master password is correct
          vault = Vault.get_vault(args.create[0], args.create[1])
          if isinstance(vault, bool):
               print(f"Incorrect master password for vault: {args.create[0]}")
     elif args.add:
          vault = Vault.get_vault(args.add[0], args.add[1])
          if isinstance(vault, bool):
               print(f"Incorrect master password for vault: {args.add[0]}")
          else:
               add_to_vault(vault, args.add[2], args.add[3], args.add[4], args.add[1])
     elif args.remove:
          vault = Vault.get_vault(args.remove[0], args.remove[1])
          if isinstance(vault, bool):
               print(f"Incorrect master password for vault: {args.remove[0]}")
          else:
               remove_from_vault(vault, args.remove[2])
     elif args.view:
          vault = Vault.get_vault(args.view[0], args.view[1])
          if isinstance(vault, bool):
               print(f"Incorrect master password for vault: {args.view[0]}")
          else:
               view_from_vault(vault, args.view[2], args.view[1])
     elif args.add_generated:
          vault = Vault.get_vault(args.add_generated[0], args.add_generated[1])
          if isinstance(vault, bool):
               print(f"Incorrect master password for vault: {args.add_generated[0]}")
          else:
               add_to_vault(vault, args.add_generated[2], make_password(), args.add_generated[3], args.add_generated[1])
     elif args.list:
          vault = Vault.get_vault(args.list[0], args.list[1])
          if isinstance(vault, bool):
               print(f"Incorrect master password for vault: {args.list[0]}")
          else:
               vault.view_all(args.list[1])
     elif args.search:
          vault = Vault.get_vault(args.search[0], args.search[1])
          if isinstance(vault, bool):
               print(f"Incorrect master password for vault: {args.search[0]}")
          else:
               results = vault.search(args.search[2])
               print(results)
     elif args.check_strength:
          vault = Vault.get_vault(args.search[0], args.search[1])
          if isinstance(vault, bool):
               print(f"Incorrect master password for vault: {args.search[0]}")
          else:
               pass
               #check_strength()
     else:
          parser.print_help()
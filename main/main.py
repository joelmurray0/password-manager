from vaultItem import VaultItem

while __name__ == "__main__":
     # object of a vault - add remove edit show functions
     # dont care about input validation for this as not problem in finished code
     master = input("enter master password")
     func = int(input("1. Add \n2. Return \n3. Delete \n4. Edit"))
     if func == 1:
          usr = input("please enter username")
          password = input("please enter password")
          url = input("what is the url of the website this account is for?")
          item = VaultItem(url, usr, password, )
     elif func == 2:
          url = input("what is the url of the website this account is for?")
     elif func == 3:
          url = input("what is the url of the website this account is for?")
     elif func == 4:
          url = input("what is the url of the website this account is for?")
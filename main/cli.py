from prettytable import prettytable
import re
import argparse

class CLIManager:
     def __init__(self, spam):
          self.spam = spam


     def run(self):
          running = True
          while running: 
               user_input = self.home_screen()
               if user_input == "1":
                    # may need to store password here for vault
                    if self.spam.get_vault(self.vault_select_name(), input("Enter vault password: ")):
                         user_input = self.vault_service_select()
                         if user_input == "1":
                              self.add_vault_item()
                         elif user_input == "2":
                              self.search()
                              
                    else:
                         print("Incorrect password")
                    
                    
               else:
                    running = False

     def search(self):
          query = input("Enter your search")
          self.spam.search(query)

     def add_vault_item(self):
          url = input("Enter url: ")
          username = input("Enter username: ")
          password = input("Enter password: ")
          self.spam.add_item(url, username, password)


     def vault_service_select(self):
          print("Choose what to do in the vault.")
          print("1. Add password")
          # print("2. Remove password")
          # print("3. Edit password")
          print("2. Search")
          print("3. List all")
          return self.input_with_validation("Choose an option: ", ["1", "2", "3"])

     def home_screen(self):
          print("welcome print") # more fancy to be added
          print("1. List vaults")
          print("2. Exit")
          return self.input_with_validation("Choose an option: ", ["1", "2"])

     def vault_select_name(self):
          vaults = self.spam.list_vaults()
          inputs = []
          for i in range(len(vaults)):
               print(f"{i+1}. {vaults[i]}")
               inputs.append(i+1)
          vault_number_shifted = int(self.input_with_validation("Choose an option: ", inputs))
          correct_vault = vaults[vault_number_shifted - 1]
          return correct_vault

     def input_with_validation(self, input_: str, expected_results: list):
          result = input(input_)
          while result not in expected_results:
               print(f"invalid input please try again - {expected_results}")
               result = input(input_)
          return result
     
     def 
# if __name__ == "__main__":
#     auth_system = AuthSystem()
#     cli = CLIManager(auth_system)
#     cli.run()
from prettytable import PrettyTable
import pyperclip 

class CLIManager:
     def __init__(self, spam):
          self.spam = spam

     def run(self):
          running = True
          self.user_state = "home"
          print()
          print("\033[1;33mAlways input the numbers in the boxes to select an option.\033[0m") # more fancy to be added
          while running:
               if self.user_state == "home":
                    self.home_screen()
               elif self.user_state == "search":
                    self.search()
               elif self.user_state == "add":
                    self.add_choice()
               elif self.user_state == "remove":
                    self.remove()
               elif self.user_state == "list":
                    self.list()
               elif self.user_state == "select_from_search":
                    self.select_from_search()
               elif self.user_state == "create_vault":
                    self.create_vault()
               else:
                    running = False

     def create_vault(self):
          name = input("Enter the name of the vault: ")
          master_password = input("Enter the master password (this cannot be changed): ")
          if self.spam.create_vault(name, master_password):
               print("Vault successfully created!")
          else:
               print("Vault already taken")
          self.user_state = "home"

     def search(self):
          query = input("Enter your search: ")
          results = self.spam.search(query)
          if results == []:
               print("There are no matches to your query.")
               self.user_state = "home"
          else:
               self.select_from_search(results)
     
     def select_from_search(self, results):
          table = PrettyTable()
          table.field_names = ["ID", "Url"]
          for i in results:
               table.add_row(i)
          print(table)
          print("To select an item enter its ID")
          inputs = ["r"]
          for i in range(len(results)):
               inputs.append(str(i+1))
          choice = self.input_with_validation("Choose an option: ", inputs)
          self.user_state = "home"
          if choice != "r":
               table = PrettyTable()
               table.field_names = ["ID", "Url"]
               table.add_row(results[int(choice) - 1])
               print(table)
               self.current_item(results[int(choice) - 1][1], results)

     def current_item(self, url, results):
          print("What do you want to do with this item (enter r to return)?")
          print("1. View")
          print("2. Edit")
          print("3. Remove")
          choice = self.input_with_validation("Choose an option: ", ["1", "2", "3", "r"])
          if choice != "r":
               if choice == "1":
                    self.show_item(url)
               elif choice == "2":
                    self.edit_item(url)
               else:
                    self.remove_item(url)
          else:
               self.select_from_search(results)

     def show_item(self, url):
          table = PrettyTable()
          table.field_names = ["Username", "Url", "Password"]
          row = self.spam.get_item(url)
          table.add_row(row)
          print(table)
          choice = self.input_with_validation("Do you want to copy to clipboard (y/n) ", ["y", "n"])
          if choice == "y":
               pyperclip.copy(row[2])

     def edit_item(self, url):
          print("What do you want to edit?")
          print("[1] Username")
          print("[2] Password")
          print("[3] Url")
          choice = self.input_with_validation("Choice: ", ["1", "2", "3"])
          item = self.spam.get_item(url)
          if choice == "1":
               item[0] = input("Enter your new username")
          elif choice == "2":
               item[2] = input("Enter your new password")
          elif choice == "3":
               item[1] = input("Enter new url")
          self.spam.remove_item(url)
          self.spam.add_item(item[1], item[0], item[2])

     def remove_item(self, url):
          self.spam.remove_item(url)
          print("Item removed!")

     def add_choice(self):
          choice = self.input_with_validation("Have generated password (y/n) ", ["y", "n"])
          if choice == "y":
               self.add(True)
          else:
               self.add(False)

     def add(self, generated):
          url = input("Enter url: ")
          username = input("Enter username: ")
          if generated:
               password = self.spam.generate_password()
          else:
               password = input("Enter password: ")
          while not self.spam.add_item(url, username, password):
               print("\033[1;31mPASSWORD TOO WEAK TO BE ADDED\033[0m")
               if generated:
                    password = self.spam.generate_password()
               else:
                    password = input("Enter password: ") 
          else:
               print("\033[1;31mPASSWORD ADDED SUCCESSFULLY\033[0m")
          self.user_state = "home"

     def list(self):
          items = self.spam.list_items()
          print("List of all items in the vault")
          table = PrettyTable()
          table.field_names = ["ID", "Url"]
          for i in items:
               table.add_row(i)
          print(table)
          self.user_state = "home"

     def home_screen(self):
          print("[1] Search Items")
          print("[2] List Items")
          print("[3] Add Items")
          print("[q] Exit")
          choice = self.input_with_validation("Choose an option: ", ["1", "2", "3", "q"])
          if choice == "1":
               self.user_state = "search"
          elif choice == "2":
               self.user_state = "list"
          elif choice == "3":
               self.user_state = "add"               
          else:
               self.user_state = "end"
                    
     def input_with_validation(self, input_: str, expected_results: list):
          result = input(input_)
          while result not in expected_results:
               print(f"Invalid input please try again - {expected_results}")
               result = input(input_)
          return result
     
if __name__ == "__main__":
    cli = CLIManager()
    cli.run()

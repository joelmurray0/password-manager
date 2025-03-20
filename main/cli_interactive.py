from prettytable import PrettyTable

class CLIManager:
     def __init__(self, spam):
          self.spam = spam

     def run(self):
          running = True
          self.user_state = "home"
          print("") # more fancy to be added
          while running:
               if self.user_state == "home":
                    self.home_screen()
               elif self.user_state == "search":
                    self.search()
               elif self.user_state == "add":
                    self.add()
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
               print("there are no matches to your query")
               self.user_state = "home"
          else:
               table = PrettyTable()
               table.field_names = ["Username", "Url", "Password"]
               for i in results:
                    table.add_row(i)
               print(table)
               self.select_from_search(results)
     
     def select_from_search(self, results):
          print("To select an item enter its ID")
          inputs = ["r"]
          for i in range(len(results)):
               inputs.append(str(i+1))
          choice = self.input_with_validation("Choose an option: ", inputs)
          if choice == "r":
               self.user_state = "home"
          else:
               self.current_item(results[int(choice) - 1])

     def current_item(self, id):
          print("What do you want to do with this item (enter b to go back)?")
          print("1. View")
          print("2. Edit")
          print("3. Remove")
          choice = self.input_with_validation("Choose an option: ", ["1", "2", "3", "b"])
          if choice != "b":
               if choice == "1":
                    self.show_item(id)
               elif choice == "2":
                    self.edit_item(id)
               else:
                    self.remove_item(id)

     def show_item(self, id):
          table = PrettyTable()
          table.field_names = ["ID", "Username", "Url", "Password"]
          table.add_row(self.spam.get_item(id))
          print(table)

     def edit_item():
          pass

     def remove_item():
          pass

     def add(self):
          url = input("Enter url: ")
          username = input("Enter username: ")
          password = input("Enter password: ")
          self.spam.add_item(url, username, password)
          self.user_state = "home"

     def remove(self):
          query = input("What password do you want to remove?")

     def list(self):
          items = self.spam.list_items()
          table = PrettyTable()
          table.field_names = ["ID", "Url"]
          for i in items:
               table.add_row(i)
          print(table)
          self.user_state = "home"

     def home_screen(self):
          print("1. Search Items")
          print("2. List Items")
          print("3. Add Items")
          print("q. Exit")
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
               print(f"invalid input please try again - {expected_results}")
               result = input(input_)
          return result
     
if __name__ == "__main__":
    cli = CLIManager()
    cli.run()

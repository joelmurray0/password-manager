import random
import re
class RandomPassword:
     def __init__(self):
          # randomly chooses length
          self._length = random.randint(16,20)

          # generates and checks password until satisfied
          self._password = self.choose_chars()
          while not self.check_requirements():
               self._password = self.choose_chars()
     
     def __str__(self):
          return self._password

     # randomly chooses characters (roughly those on the keyboard) for the length chosen
     def choose_chars(self):
          temp = ""
          self._symbol_type_dict = {}
          for _ in range(self._length):
               rand_num = random.randint(33, 126)
               char = chr(rand_num)
               temp += char
          return temp
     
     # Uses regex to check that password requirements are satisfied
     def check_requirements(self):
          requirements = r"^(?=(?:.*[a-z]){8,})(?=(?:.*[A-Z]){2,})(?=(?:.*\d){2,})(?=(?:.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]){4,}).*$"
          return bool(re.match(requirements, self._password))
     
password = RandomPassword()
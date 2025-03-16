import random
import re

def make_password():
     # randomly chooses length
     length = random.randint(16,20)

     # generates and checks password until satisfied
     password = choose_chars(length)
     while not check_requirements(password):
          password = choose_chars(length)
     return password

# randomly chooses characters (roughly those on the keyboard) for the length chosen
def choose_chars(length):
     temp = ""
     for _ in range(length):
          rand_num = random.randint(33, 126)
          char = chr(rand_num)
          temp += char
     return temp

# Uses regex to check that password requirements are satisfied
def check_requirements(password):
     requirements = r"^(?=(?:.*[a-z]){8,})(?=(?:.*[A-Z]){2,})(?=(?:.*\d){2,})(?=(?:.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]){4,}).*$"
     
     return bool(re.match(requirements, password))
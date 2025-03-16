ui = {}
ui["a"].append(1)
print(ui["a"] == None)
print(ui)
# produce key error if not in dict
x = [2,3,1,3,1]
print(set(x))

a = int("1010",2)
b = int("0001", 2)
print(a+b)

#print(a[:2])
#print(b[1])
def replace_with_a(s: str):
    result = []
    for i in range(len(s)):
        new_s = s[:i] + 'b' + s[i+1:]
        result.append(new_s)
    return result

# Example usage:
original_string = ""
output = replace_with_a(original_string)
#print(output)


def unduplicate_token_table(self, arr2d):
     temp_dict = {}
     for i in arr2d:
          #print(temp_dict)
          if i[0] in temp_dict:
               print(i)
               current = temp_dict[i[0]]
               current.extend(i[1])
               temp_dict[i[0]] = current
          else:
               temp_dict[i[0]] = i[1]
     return [[key, value] for key, value in temp_dict.items()]


x = [
       ["a", [1]],
       ["a", [4]],
       ["a", [3,2]],
       ["b", [4]],
       ["c", [1]]
]

#print(unduplicate_token_table(x))
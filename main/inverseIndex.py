class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class InverseIndex:
     def __init__(self, arr = []):
          self.head = None
          # self.create(arr)

     # def create(self, arr):
     #      if arr != []:
     #           for i in arr:
     #                self.add(i[0], i[1])

     def add(self, string, id):
          data = [string, id]
          new_node = Node(data)

          if not self.head or self.head.data[0] > data[0]: # checks if first in the list
               new_node.next = self.head
               self.head = new_node
          else:
               current = self.head
               while current.next != None and current.data[0] < data[0]:
                    current = current.next
               if current.next == None:
                    current.next = new_node
                    new_node.next = None
               elif current.next.data[0] > data[0]:
                    new_node.next = current.next
                    current.next = new_node
               else:
                    temp = current.data[1]
                    temp.extend(data[1])
                    current.data[1] = list(set(temp))
               
                    
                    
     


          # if not self.head or self.head.data[0] > data[0]:
          #      new_node.next = self.head
          #      self.head = new_node
          #      return
          # current = self.head
          # while current.next != None and current.data[0] < data[0]:
          #      current = current.next
          # if current.next == None and current.data[0] > data[0]:
          #      current.next = new_node
          #      new_node.next = None
          # elif current.next == None and current.data[0] == data[0]:
          #      temp = current.data[1]
          #      temp.extend(data[1])
          #      current.data[1] = list(set(temp))
          # else:
          #      new_node.next = current.next
          #      current.next = new_node

     def delete(self, id):
          temp = self.head
          prev = None
          while temp != None:
               if id in temp.data[1]:
                    temp.data[1].remove(id)
                    if temp.data[1] == []:
                         prev.next = temp.next
               prev = temp
               temp = temp.next

     def search(self, target):
          temp = self.head
          while temp != None:
               if temp.data[0] == target:
                    print(f" found {temp.data[0]}, result {temp.data[1]}")
                    return temp.data[1]
               temp = temp.next

     def display(self):
          current = self.head
          while current:
               print(current.data, end=" -> ")
               current = current.next
          print("None")
     
     # def save(self): # turns into 2d array to reconstruct linked list
     #      arr = []
     #      temp = self.head
     #      while temp is not None:
     #           arr.append(temp.data)
     #           temp = temp.next
     #      return arr

# x = InverseIndex()
# x.add(["google", [1]])
# x.add(["bing", [2]])
# x.add(["a", [0]])
# x.add(["a", [2]])
# print()
# print(x.search("a"))
# print()
# x.display()
# x.delete(2)
# x.display()
# print()
# print(x.search("a"))
# print()

# x.add("string", 1)
# x.add("string", 2)
# x.display()


# inverse_index = InverseIndex()
# inverse_index.add("stringa", 1)
# inverse_index.add("stringb", 2)
# inverse_index.display()

inverse_index = InverseIndex()
inverse_index.add("c", [1])
inverse_index.add("e", [1])
inverse_index.add("a", [1])
# inverse_index.add("d", [1]) # middle
# inverse_index.add("f", [1])
inverse_index.display()
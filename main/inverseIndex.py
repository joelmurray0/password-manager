class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class InverseIndex:
     def __init__(self):
          self.head = None

     def add(self, string, id):
          data = [string, [id]]
          new_node = Node(data)
          if not self.head or self.head.data[0] > data[0]:
               new_node.next = self.head
               self.head = new_node
               return
          current = self.head
          while current.next != None and current.data[0] < data[0]:
               current = current.next
          if current.next == None and current.data[0] > data[0]:
               current.next = new_node
               new_node.next = None
          elif current.next == None and current.data[0] == data[0]:
               temp = current.data[1]
               temp.extend(data[1])
               current.data[1] = list(set(temp))
          else:
               new_node.next = current.next
               current.next = new_node

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
          found = False
          temp = self.head
          while not found and temp != None:
               if temp.data[0] == target:
                    return temp.data[1]
               temp = temp.next

     def display(self):
          current = self.head
          while current:
               print(current.data, end=" -> ")
               current = current.next
          print("None")


x = InverseIndex()
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


inverse_index = InverseIndex()
inverse_index.add("stringa", 1)
inverse_index.add("stringb", 2)
inverse_index.display()
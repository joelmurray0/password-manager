# can be improved knowing that the first part of the list is already sorted O(nlog(n))
def merge_sort(arr):
     if len(arr) <= 1:
          return arr
     
     mid = len(arr) // 2
     left_half = merge_sort(arr[:mid])
     right_half = merge_sort(arr[mid:])
     
     return merge(left_half, right_half)

def merge(l, r):
     sorted_arr = []
     i = j = 0
     
     while i < len(l) and j < len(r):
          if l[i] < r[j]:
               sorted_arr.append(l[i])
               i += 1
          # another good reason for reverse tables and this table so dont get merged :)

          # IN THE MERGE IS HARD AND MAYBE NOT GREAT
          # elif l[i] == r[j]: 
          #      print()
          #      print(l[i][1], r[j][1])
          #      l[i][1].extend(r[j][1])
          #      print()
          #      print(l[i][1])
          #      combin = list(set(l[i][1]))
          #      temp = list(set(combin))
          #      sorted_arr.append(temp)
          #      print(sorted_arr)
          #      i += 1
          #      j += 1
          else:
               sorted_arr.append(r[j])
               j += 1
     
     sorted_arr.extend(l[i:])
     sorted_arr.extend(r[j:])
     
     return sorted_arr
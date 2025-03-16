def binary_search_arr2d(arr2d, query):
     midpoint = len(arr2d)//2
     if query > arr2d[midpoint][0]:
          return binary_search_arr2d(arr2d[midpoint:], query) + midpoint
     elif query < arr2d[midpoint][0]:
          arr2d[:midpoint]
          return binary_search_arr2d(arr2d[:midpoint], query)
     else:
          return midpoint
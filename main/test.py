data = ["1","2","pass"]
d1 = data[0].encode()
d2 = data[1].encode()
print("0".encode()+d1+d2)

print(d1)
print(d2)
print((d1) | (d2))
def binary_to_bytes(binary_int: int): # only takes multiples of 8 - increases space efficiency by 8 times
     # Initializing a binary string in the form of
     # 0 and 1, with base of 2
     
     # Getting the byte number
     byte_number = (binary_int.bit_length() + 7) // 8
     
     # Getting an array of bytes
     binary_array = binary_int.to_bytes(byte_number, "big")
     
     # Converting the array into ASCII text
     ascii_text = binary_array.decode()
     
     # Getting the ASCII value
     return ascii_text

def ascii_to_binary(text):
    # Convert each character to its binary representation
    binary_string = ''.join(format(ord(char), '08b') for char in text)
    return binary_string

text = binary_to_bytes(int("00100101", 2))
print(ascii_to_binary(text))
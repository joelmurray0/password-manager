def right_shift(bits: str, n: int):
     return n*"0" + bits[:-n]

def right_rotation(bits: str, n: int):
     return bits[-n:] + bits[:-n]

def xor(x, y):
     if len(x) != len(y):
          return False
     output = ""
     for i in range(1, len(x) + 1):
          if x[-i] == y[-i]:
               output += "0"
          else:
               output += "1"
     return output

def maj(x,y,z):
     output = ""
     for i in range(1, 1+len(x)):
          if int(x[-i]) + int(y[-i]) + int(z[-i]) >= 2:
               output += "1"
          else:
               output += "0"
     return output

def ch(x,y,z):
     output = ""
     for i in range(1, 1+len(x)):
          if x[-i] == "0":
               output += z[-i]
          else:
               output += y[-i]
     return output

def lower_sigma_0(bits_32: str):
     rot_7 = right_rotation(bits_32, 7)
     rot_18 = right_rotation(bits_32, 18)
     shift_3 = right_shift(bits_32, 3)
     return xor(shift_3, xor(rot_7, rot_18))

def upper_sigma_0(bits):
     rot_2 = right_rotation(bits, 2)
     rot_13 = right_rotation(bits, 13)
     rot_22 = right_rotation(bits, 22)
     return xor(rot_22, xor(rot_13, rot_2))

def lower_sigma_1(bits_32):
     rot_17 = bits_32[15:] + bits_32[:15]
     rot_19 = bits_32[13:] + bits_32[:13]
     shift_10 = right_shift(bits_32, 10)

def upper_sigma_1(bits):
     rot_6 = right_rotation(bits, 6)
     rot_11 = right_rotation(bits, 11)
     rot_25 = right_rotation(bits, 25)
     return xor(rot_25, xor(rot_11, rot_6))

def w_t(bit_string_512, t):
     return str(bin(lower_sigma_1(bit_string_512[t-2])) + bin(bit_string_512[t-7]) + bin(lower_sigma_0(bit_string_512[t-15])) + bin(bit_string_512[t-16]))

def preprocess(raw: str):
     original = raw
     raw += "1"
     while len(raw) % 512 != 448:
          raw += "0"
     raw += original.zfill(64)
     return raw

def bit_blocks_512(padded_bit_string: str):
     return [padded_bit_string[512*i:512*(i+1)] for i in range(len(padded_bit_string)//512)]

def bit_chunk_32(bit_string_512):
     return [bit_string_512[32*i:32*(i+1)] for i in range(16)]

def sha_256(bit_string):
     padded_bit_string = preprocess(bit_string)
     bit_string_512_chunks = bit_blocks_512(padded_bit_string)
     for i in range(len(bit_string_512_chunks)):
          bit_string_512_chunks[i] = bit_chunk_32(bit_string_512_chunks[i])
     working_variables = []
     for bit_string_512 in bit_string_512_chunks:
          working_variables.append(w_t(bit_string_512, 16))

     t_1 = working_variables[7] + upper_sigma_1(working_variables[4]) + ch(working_variables[4], working_variables[5], working_variables[6]) + 
     print(bit_string_512_chunks)
     print(len(padded_bit_string))

#sha_256("1010")
# could use hamming codes for the search instead?? - could do both
mistype_letters = {
     "a": "qwsz",
     "b": "vghn ",
     "c": "xdfv ",
     "d": "swerfcx",
     "e": "wsdfr",
     "f": "dertgvc",
     "g": "frtyhbv",
     "h": "gtyujnb",
     "i": "ujko",
     "j": "hyukmn",
     "k": "juilom",
     "l": "kiop",
     "m": "njkl ",
     "n": "bhjm ",
     "o": "iklp",
     "p": "ol;[09-=]",
     "q": "wsa21`",
     "r": "45edfgt",
     "s": "qwadxze",
     "t": "56ryhfg",
     "u": "yihkj78",
     "v": "cdfgb ",
     "w": "qased23",
     "x": "zsdc ",
     "y": "tguhj67",
     "z": r'as\x'
}

def fuzzy_tokens(str, id, swaps=mistype_letters):
     output = []
     list_str = []
     for char in str:
          list_str.append(char)

     for i in range(len(str)): # does 1 mistake
          for swap in swaps[str[i]]:
               new_str = str[:i] + swap + str[i+1:]
               output.append([new_str, id])
     return output
import string
from nltk.util import ngrams
#from fuzzy import Soundex

def generate_tokens(word, id, n_min=2, n_max=6):
     result = generate_fuzzy_deletions(word)
     result.extend(generate_fuzzy_insertions(word))
     result.extend(generate_fuzzy_substitutions(word))
     result.extend(generate_variable_ngrams(word, n_min, n_max))
     result = list(set(result))
     for i in range(len(result)):
          result[i] = [result[i], id]
     return result

def generate_fuzzy_insertions(word):
     letters = string.ascii_lowercase
     variations = set()

     # Insertions
     for i in range(len(word) + 1):
          for letter in letters:
               variations.add(word[:i] + letter + word[i:])

     return [i for i in list(variations)]

def generate_fuzzy_deletions(word):
     variations = set()

     # Deletions
     for i in range(len(word)):
          variations.add(word[:i] + word[i+1:])
     
     return [i for i in list(variations)]

def generate_fuzzy_substitutions(word):
     letters = string.ascii_lowercase
     variations = set()

     # Substitutions
     for i in range(len(word)):
          for letter in letters:
               if word[i] != letter:
                    variations.add(word[:i] + letter + word[i+1:])

     return [i for i in list(variations)]

def generate_ngrams( word, n): # does not check for duplicates - keep in mind
     return [''.join(gram) for gram in ngrams(word, n)]

def generate_variable_ngrams(word, min_n=2, max_n=6):
     result = []
     for n in range(min_n, min(max_n, len(word))+1):
          for i in generate_ngrams(word, n):
               result.append(i)
     return result


     # soundex = Soundex()

     # def generate_phonetic_matches(word, dictionary):
     #      target_soundex = soundex(word)
     #      return [w for w in dictionary if soundex(w) == target_soundex]

# results = generate_variable_ngrams("eletters", 1)
# print(results)
# print(len(results))
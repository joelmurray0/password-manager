import string
from nltk.util import ngrams
from urllib.parse import urlparse
#from fuzzy import Soundex

import tldextract
from urllib.parse import urlparse, parse_qs

def extract_url_parts(url, id):

     if "://" not in url:
          url = "https://" + url
     result = []    
     # Parse the URL
     parsed = urlparse(url)
     
     # Extract domain parts
     extracted = tldextract.extract(parsed.netloc)
     # print(tldextract.extract(parsed.netloc))
     # print(extracted.subdomain.split("."))
     
     # Remove "www" if present in subdomain
     subdomains = [part for part in extracted.subdomain.split(".") if part and part != "www"]
     
     whole = subdomains
     whole.append(extracted.domain)
     whole.append(extracted.suffix)
     # Construct full domain
     domain_no_www = ".".join(filter(None, whole))

     domain_no_subdomain = ".".join(filter(None, [extracted.domain, extracted.suffix]))

     # Extract path parts, removing empty strings
     path_parts = [part for part in parsed.path.split("/") if part]

     query_params = parse_qs(parsed.query)
    
     # print(domain_no_www)
     # print(subdomains)
     # print(query_params)
     # print(path_parts)

     result.append([extracted.domain, [id]])
     if domain_no_www != domain_no_subdomain:
          result.append([domain_no_www, [id]])
     result.append([domain_no_subdomain, [id]])
     for subs in subdomains:
          result.append([subs, [id]])
     if len(path_parts) != 0:
          for part in path_parts:
               result.append([part, [id]])
     if "q" in query_params:
          result.append([query_params["q"], [id]])

     return result

def generate_tokens(word, id, n_min=2, n_max=6):
     result = generate_fuzzy_deletions(word)
     result.extend(generate_fuzzy_insertions(word))
     result.extend(generate_fuzzy_substitutions(word))
     result.extend(generate_variable_ngrams(word, n_min, n_max))
     result = list(set(result))
     for i in range(len(result)):
          result[i] = [result[i], id]
     return result

def generate_url_parse(url, id):
     parsed_url = urlparse(url)
     token = []
     for section in parsed_url:
          if section != None and section != "":
               token.append([section, [id]])
     return token
     
     token.append([parsed_url.hostname, [id]])
     token.append([parsed_url.hostname, [id]])

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
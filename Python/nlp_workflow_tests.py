# NLP (bag of words approach)
# pre-proccessing flow: 
# make it lower case; tokenize; remove stopwords; word stemming; remove punctuation; strip out html tags.

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# import nltk.tokenize.punkt
from bs4 import BeautifulSoup

sentence = 'Almost before we knew it, we had left the ground.'

# lower casing + tokenizing
tokenized_sentence =  set(word_tokenize(sentence.lower())) # function from nltk.tokenize
print('TOKENIZED, LOWER CASED SENTENCE:\n', tokenized_sentence)

# remove stopwords using the set data structure
eng_stop_words = set(stopwords.words('english')) # store stopwords from nltk.corpus.stopwords to a set
print('ENGLISH STOP WORDS:\n', eng_stop_words)

filtered_set = tokenized_sentence.difference(eng_stop_words) # https://www.w3schools.com/python/python_sets_methods.asp
print('FILTERED SENTENCE:\n', filtered_set)

# stemming words
stemmer = PorterStemmer()

dummy_set = set(('weakness', 'temptations', 'requires', 'courage')) # dummy set of 'stemmable' words
dummy_set.update(filtered_set) # "Update the set with the union of this set and others"

stemmed_set = [stemmer.stem(word) for word in dummy_set]
print('SET AFTER WORD STEMMING:\n', stemmed_set)

# removing punctuation
no_punctuation_set = set(filter(lambda word: word.isalpha(), stemmed_set))
print('PUNCTIATION REMOVED:\n', no_punctuation_set)

# remove HTML tags using Beautiful Soup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
FILE_PATH = 'dirty_html_content.txt' # file containing some html for tests
tagged_message = open(FILE_PATH).read()
# print('EMAIL WITH DIRTY HTML TAGS:\n', tagged_message)
soup = BeautifulSoup(tagged_message, 'html.parser')
print('EMAIL WITH HTML TAGS REMOVED:\n', soup.get_text())
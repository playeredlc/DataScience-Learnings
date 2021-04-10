import nltk
from nltk.stem import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup

def clean_message(message, stemmer=PorterStemmer(), stop_words=stopwords.words('english')):

	"""
		Applies basic NLP workflow in the email message:
		Strips out HTML tags, tokenize, remove stop words, word stemming and remove punctuation.
		Returns a clean set of tokens.

		Args:
			clean_message	: The message to be processed and cleaned.
			stemmer 		: The stem method to be used. Default is PorterStemmer().
			stop_words		: The stop words list to use. Default is stopwords.words('english') from NLTK.

	"""

	# remove HTML tags
	soup = BeautifulSoup(message, 'html.parser')
	message = soup.get_text()
	
	tokens = set(word_tokenize(message.lower())) # lower + tokenize
	tokens = tokens.difference(set(stop_words))	# remove stop words
	tokens = [stemmer.stem(token) for token in tokens] # word stemming
	tokens = set(filter(lambda token: token.isalpha(), tokens)) # remove punctuation

	return tokens


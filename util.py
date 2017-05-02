import nltk
import string

#
# This method is basically reading files (in this case, the file is specifically for Twecoll),
# and finding three main things: date, user, and tweet content.
# The method returns an two dimensional array: 
# 1st dimension is document
# 2nd dimension is date, user, and content.
# 
# by Bima :)
def extract(filename):

	dataset = open(filename, 'r')


	lines = dataset.read().split('\n') # Spliting per line


	# Splitting per date, user, link and content; and put it into a(n) file/array

	dataset_arr = []

	for line in lines:

		words = line.split(' ') 

		i = 0
		date = user = tweet = link = ''

		for word in words:
			if i in range (0, 6):
				date = date + ' ' + word
			elif i == 6:
				user = word
			else:
				tweet = tweet + ' ' + word
			i += 1

		dataset_arr.append([date.strip(), user, tweet.strip()])

	dataset.close()

	return dataset_arr

#
# This method is generating bag of words from each tweet.
# The method returns array consisting of bag of words from each tweet 
#
# by Bima :)
def tokenize(dataset):

	bags_of_words = []

	printable = set(string.printable)

	for line in dataset_arr:
		tokens = nltk.word_tokenize(filter(lambda x: x in printable, line[2])) # tokenizing needs to throw all ASCII code away. hence, the lambda function

		bags_of_words.append(tokens)

	return bags_of_words

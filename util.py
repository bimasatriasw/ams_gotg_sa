import nltk
import string
import numpy as np
import scipy

from nltk.corpus import stopwords

#
# This method is basically reading files (in this case, the file is specifically for Twecoll),
# and finding three main things: date, user, and tweet content.
# The method returns an two dimensional array: 
# 1st dimension is document
# 2nd dimension is date, user, and content.
# 
def extract(filename):

	dataset = open(filename, 'r')


	lines = dataset.read().split('\n') # Spliting per line


	# Splitting per date, user, link and content; and put it into a(n) file/array

	dataset_arr = []

	for line in lines:

		lines2 = line.split('#tagnyajadi#')
		words = lines2[0].split(' ') 

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

		# Filtering emojis
		printable = set(string.printable)
		tweet = filter(lambda x: x in printable, tweet)

		dataset_arr.append([date.strip(), user, tweet.strip(), lines2[1]])

	dataset.close()

	return dataset_arr


#
# Membuang stopwords dari konten dataset
#
def filter_stopwords(dataset):

	stop = set(stopwords.words('english'))

	for data in dataset:

		filtered_content = ''

		for word in data[2].split():

			if word.lower() not in stop:
				filtered_content = filtered_content + ' ' + word

		data[2] = filtered_content

	return dataset

#
# Memberi nilai dari kalimat pada tiap data menggunakan sentiment lexicon
# Akan mengembalikan list nilai dari masing-masing data
#
def sentiment_checker(dataset):

	positive_words = np.array(file('corpus/positive-words.txt', 'r').read().split('\n'))
	negative_words = np.array(file('corpus/negative-words.txt', 'r').read().split('\n'))

	score_array = []

	for data in dataset:
		
		tokens = nltk.word_tokenize(data[2])
		score = 0
		
		for token in tokens:
		 	if token.lower() in positive_words:
		 		score += 1
		 	elif token.lower() in negative_words:
		 		score -= 1

		score_array.append(score)
		
	return score_array

#
# Joining feature to existing vector
#
def add_feature(vectors, feature):

	i = 0
	for vector in vectors:
		vector.append(feature[i])
		print i
		i += 1

	vectors = scipy.sparse.csr_matrix(np.array(vectors).astype(float))

	return vectors


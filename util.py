import nltk
import string

from nltk.corpus import stopwords

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
# Membuang stopwords dari konten dataset
#
# by Bima :)
def filter_stopwords(dataset):

	stop = set(stopwords.words('english'))

	for data in dataset:

		filtered_content = ''

		for word in data[2].split():

			if word.lower() not in stop:
				filtered_content = filtered_content + ' ' + word

		data[2] = filtered_content

	return dataset




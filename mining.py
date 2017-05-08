import util
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# 1. DATA SET EXTRACTION

dataset = util.extract('dataset/twitter-full')


# 2. PRE-PROCESSING

dataset = util.filter_stopwords(dataset)
content = np.array(dataset)


# 3. REPRESENTATION (kemungkinan bentuk vektor dengan mungkin ada tambahan fitur lain)

# # Pilihan metode representasi vektor # #
# vectorizer = CountVectorizer()
vectorizer = TfidfVectorizer()
vector = vectorizer.fit_transform(content[:, 2])


# 4. BUILDING MODEL







# # FOR CHECKING
# print content[:, 2]
# for v in vector:
# 	print v
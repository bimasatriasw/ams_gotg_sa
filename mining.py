import util
import numpy as np
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from scipy.sparse import hstack, coo_matrix


# 1. DATA SET EXTRACTION

dataset = util.extract('dataset/twitter')



# 2. PRE-PROCESSING

dataset = util.filter_stopwords(dataset)
content = np.array(dataset)



# 3. REPRESENTATION (kemungkinan bentuk vektor dengan mungkin ada tambahan fitur lain)

np.random.shuffle(content)
training, testing = content[:70,:], content[70:,:]

# # Pilihan metode representasi vektor # #

# vectorizer = CountVectorizer()
vectorizer = TfidfVectorizer()

vector_training = vectorizer.fit_transform(training[:, 2]).toarray().tolist() # training
label_training = training[:,3]

vector_testing = vectorizer.transform(testing[:, 2]).toarray().tolist() # testing
label_testing = testing[:,3]

# # Adding sentiment checker feature

# Training
sentiment_score = util.sentiment_checker(training)
vector_training = util.add_feature(vector_training, sentiment_score)

# Testing
sentiment_score = util.sentiment_checker(testing)
vector_testing = util.add_feature(vector_testing, sentiment_score)



# 4. BUILDING MODEL

# # kita gunakan model logistic regression
# clf = LogisticRegression().fit(vector, label)
# clf = MultinomialNB().fit(vector, label)
clf = KNeighborsClassifier(n_neighbors=3).fit(vector_training, label_training)



# 5. TESTING THE MODEL

# beri label testing data terlebih dahulu
Y_predicted = clf.predict(vector_testing)

##### metrics evaluasi #####
# hitung score, bandingkan hasil label prediksi, dengan label sesungguhnya di testing data
# --> tampilkan nilai accuracy
accuracy = accuracy_score(label_testing, Y_predicted)
print 'accuracy : ', accuracy

# --> metric lebih detail: precision, recall, f1
report = classification_report(label_testing, Y_predicted)
print '\nprecision, recall, f1:'
print report

# --> confusion matrix
print '\nconfusion matrix:'
print confusion_matrix(label_testing, Y_predicted)

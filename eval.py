from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np
import util
import pickle


# load testing data
dataset = util.extract('dataset/twitter-testing')

dataset = np.array(util.filter_stopwords(dataset))

vectorizer = TfidfVectorizer()
vector = vectorizer.transform(dataset[:, 2])


# Kita muat kembali model yang sudah kita latih sebelumnya
loaded_model = pickle.load(open('testing.model', 'rb'))

# beri label testing data terlebih dahulu
Y_predicted = loaded_model.predict(vector)


##### metrics evaluasi #####
# hitung score, bandingkan hasil label prediksi, dengan label sesungguhnya di testing data
# --> tampilkan nilai accuracy
accuracy = accuracy_score(dataset[:, 3], Y_predicted)
print 'accuracy : ', accuracy

# --> metric lebih detail: precision, recall, f1
report = classification_report(dataset[:, 3], Y_predicted)
print '\nprecision, recall, f1:'
print report

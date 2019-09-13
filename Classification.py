'''
    Author: Rishab Lalwani
    Title: Performing classification and natural language processing on subreddits
'''
import nltk
import pandas as pd
from autocorrect import spell
import re
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix
from sklearn.multiclass import OneVsRestClassifier

nltk.download('punkt')
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#Import json files using pandas
df1 = pd.read_json('subreddit1.json', orient='split')
df2 = pd.read_json('subreddit2.json', orient='split')
df3 = pd.read_json('subreddit3.json', orient='split')

# Concatenating 3 subreddits for classification
# frames=[df2,df1]
frames = [df1,df3, df2]
result = pd.concat(frames,sort=False)
# Performing classification based on titles of the subreddit
titles=result.loc[:,'title']
dat=[]

#Experiment w/ feature engineering: lemmatize and stemming raw data, or remove stop words
for i in titles:
    sms = re.sub('[^A-Za-z]', ' ', i)
    sms = sms.lower()
    tokenized_sms = word_tokenize(sms)
    for word in tokenized_sms:
        if word in stopwords.words('english'):
            tokenized_sms.remove(word)
    stemmer = PorterStemmer()
    for i in range(len(tokenized_sms)):
        tokenized_sms[i] = stemmer.stem(tokenized_sms[i])
        tokenized_sms[i] = stemmer.stem(spell(tokenized_sms[i]))
    tokenized_sms = ' '.join(tokenized_sms)
    dat.append(tokenized_sms)


#Vectorization of dataframe
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features=100)
# Without natural language processing
vector_X_un = vectorizer.fit_transform(titles).toarray()
# With natural language processing
vector_X = vectorizer.fit_transform(dat).toarray()
vector_Y = vectorizer.fit_transform(result.loc[:,'dataset']).toarray()

#Training SVM
from sklearn.model_selection import train_test_split
#change

x_train, x_test, y_train, y_test = train_test_split(vector_X,result.loc[:,'dataset'],test_size = 0.5, random_state = 0)
# train_x, test_x, train_y, test_y = train_test_split(x_test,y_test,test_size = 0.5, random_state = 0)

from sklearn.svm import SVC
svc = OneVsRestClassifier(SVC(kernel='linear',probability=True))
S=svc.fit(x_train,y_train)

y_pred_s = svc.predict(x_test)

#Training with development ( 50% + 25% )
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(vector_X,vector_Y,test_size = 0.25, random_state = 0)

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X_train, Y_train)

y_pred_r = clf.predict(X_test)


#My-Testing
print('------Statistics------','\n'*3)
c=0
y_tester=y_test.values.tolist()
for i in range(len(y_pred_s)):
    if y_tester[i]==y_pred_s[i]:
        c+=1
print('SVM','\n','Confusion matrix for SVM:','\n',confusion_matrix(y_test,y_pred_s))
print()
print('Classification Report:','\n', classification_report(y_test,y_pred_s))
print('Support Vector Classifier accuracy:',c*100/len(y_pred_s),'%')
print()
print('Random Forest','\n','Confusion matrix for RandomForest:','\n',confusion_matrix(Y_test.argmax(axis=1),y_pred_r.argmax(axis=1)))
print()
print('Classification Report:','\n',classification_report(Y_test.argmax(axis=1),y_pred_r.argmax(axis=1)))
print('Random Forest Classifier accuracy:',accuracy_score(Y_test,y_pred_r)*100,'%')




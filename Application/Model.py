import numpy as np
import pandas as pd
import pickle
from sklearn.naive_bayes import MultinomialNB
from nltk.stem import PorterStemmer 
from sklearn.feature_extraction.text import CountVectorizer

# Loading model from pickle
with open('.//Pickles//MultinomialNBmodel.pickle','rb') as file:
    _model=pickle.load(file)

# Loading stopwords & punctuation from pickle
with open('.//Pickles//stopwords&punctuation.pickle','rb') as file:
    stopWords,punctuation=pickle.load(file)

# Loading vectorizer from pickle
with open('.//Pickles//vectorizer.pickle','rb') as file:
    vectorizer =pickle.load(file)

# Defining process_text
ps = PorterStemmer()

def process_text(text):
    '''
    1. Remove punctuation
    2. Remove stopwords
    3. stem the text
    4. Return array of stammed_words
    '''
    #1
    nopunc = [char for char in text if char not in punctuation]
    nopunc = ''.join(nopunc)
    
    #2
    clean_words = [word for word in nopunc.split() if word.lower() not in stopWords]
    
    #3
    stammed_words=[ps.stem(word) for word in clean_words]
    
    #4
    return ' '.join(stammed_words)

# Defining the main logic function
def validate(text):
    if text=='':
#         print('No input')
        return 'No input'.upper()
    else:
        text=process_text(text)
#         print(text)
        x = vectorizer.transform([text])
        y_pred = _model.predict(x)
        return y_pred[0].upper()



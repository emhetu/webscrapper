
import random
import csv
import nltk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import WordNetLemmatizer
with open('Allheadlines.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        example_text = row[0]
        tokenized = word_tokenize(example_text.lower())
        stop_words = set(stopwords.words("English"))
        filtered_sentence = [w for w in tokenized if not w in stop_words]
        all_words = filtered_sentence.WordNetLemmatizer()
        alll_words = nltk.FreqDist(all_words)
        print(alll_words.most_common(3))
        
        
        
        
    
        
        
       
      

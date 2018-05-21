import random
from nltk.corpus import movie_reviews
import csv
import nltk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords
with open('Allheadlines.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        example_text = row[0]
        tokenized = word_tokenize(example_text.lower())
        stop_words = set(stopwords.words("English"))
        filtered_sentence = [w for w in tokenized if not w in stop_words]
        print(filtered_sentence)
        
        

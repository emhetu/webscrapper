import csv
import nltk
from nltk import word_tokenize
#from replacers import RegexpReplacer
from nltk.corpus import stopwords
with open('Allheadlines.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        example_text = row[0]
        All_lowercase = example_text.lower()
        print(All_lowercase)

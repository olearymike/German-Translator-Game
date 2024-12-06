# Take a CSV file with multiple categories: German Word, English Equivalent, and PoS

# A game that gives you an English word and asks for the German equivalent, kinda like Quizlet
# Also like Quizlet, it keeps track of which words you aren't as familiar with

# Uses Panda and Plotly to show your learning statistics (What PoS you need most help with)

# There will be another mode where you are given an English sentence and you must translate it
# The sentences will be randomly generated. It will start off using simple phrases like "Die blau Katze läuft"
import csv
from random import randint

with open('lernen/dictionary.csv', 'r') as file:
    dictionary = list(csv.reader(file))
    
    while True:
        index = randint(1,len(dictionary)-1)
        word = dictionary[index][1]
        
        print('Was ist das: ' +  word)

        while True:

            attempt = input()

            if attempt == dictionary[index][3]:
                print('Genau')
                break
            else:
                print('Nochmal, was ist das: ' + word)

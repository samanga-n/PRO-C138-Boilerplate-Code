#Text Data Preprocessing Lib
import nltk

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

import json
import pickle
import numpy as np

words=[]
classes = []
word_tags_list = []
ignore_words = ['?', '!',',','.', "'s", "'m"]
train_data_file = open('intents.json').read()
intents = json.loads(train_data_file)

# function for appending stem words
def get_stem_words(words, ignore_words):
    stem_words = []
    for word in words:
        if word not in ignore_words:
            w = stemmer.stem(word.lower())
            stem_words.append(w)  
    return stem_words

for intent in intents['intents']:
    
        # Add all words of patterns to list
        for pattern in intent['patterns']:            
            pattern_word = nltk.word_tokenize(pattern)            
            words.extend(pattern_word)                      
            word_tags_list.append((pattern_word, intent['tag']))
        # Add all tags to the classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
            stem_words = get_stem_words(words, ignore_words)

print(stem_words)
print(word_tags_list[0]) 
print(classes)   

#Create word corpus for chatbot
def create_bot_corpus(stem_words, classes):

    stem_words = sorted(list(set(stem_words)))
    classes = sorted(list(set(classes)))

    pickle.dump(stem_words, open('words.pkl','wb'))
    pickle.dump(classes, open('classes.pkl','wb'))

    return stem_words, classes

stem_words, classes = create_bot_corpus(stem_words,classes)  

print(stem_words)
print(classes)

#Create Bag Of Words
training_data = []
number_of_tags = len(classes)
labels = [0]*number_of_tags

# Create bag od words and labels_encoding
for word_tags in word_tags_list:
        
        bag_of_words = []       
        pattern_words = word_tags[0]
       
        for word in pattern_words:
            index=pattern_words.index(word)
              

        for word in stem_words:
            if word in pattern_words:
                bag_of_words.append(1)
            else:
                bag_of_words.append(0)
        print(bag_of_words)

         #labels all zeroes initially
    
        #save tag
        
        #go to index of tag
        
        #append 1 at that index
       
        training_data.append([bag_of_words, labels_encoding])

print(training_data[0])

# Create training data
def preprocess_train_data(training_data):
   
    training_data = np.array(training_data, dtype=object)
    
    train_x = list(training_data[:,0])
    train_y = list(training_data[:,1])

    

train_x, train_y = preprocess_train_data(training_data)
#Create training data

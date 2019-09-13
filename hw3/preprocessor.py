'''
Author: Dipesh Gautam
E-Mail: dgautam@memphis.edu

This module preprocesses the Raw text and
obtain the pos tags using NLTK
'''

import nltk
from nltk import pos_tag, word_tokenize
rawfile = open("news_25_sentences.txt")
testfile = open("news_25_tagged_sentences.txt","w")
firstsentence = True
for line in rawfile:
    line = line.strip(" \r\n")
    tokens = word_tokenize(line)
    #print(tokens)
    tagged_words = nltk.pos_tag(tokens)
    
    if(len(tagged_words) > 0 and not firstsentence):
        testfile.write("\n")
    firstword = True  
    for entry in tagged_words:
        word = entry[0]
        tag = entry[1]
        if firstword:
            testfile.write(tag + " " + word)
            firstword = False
        else:
            testfile.write(" " + tag + " " + word)
        firstsentence = False
        #tag_word += tag + " " + word
        #print(tag_word)
        
    

rawfile.close()
testfile.close()

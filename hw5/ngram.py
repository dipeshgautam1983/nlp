'''
Author: Dipesh Gautam
e-mail: dgautam@memphis.edu

This class implements the constructor to extract n-grams from the given text.
The text may be list of sentences or a single sentence.
The 'throwpunctuation' parameter controls whether to discard or consider punctuation
The 'takesentstartstop' parameter controls whether to consider start and stop symbol of the sentence;
for example a bigram could be *_the or wall_* if the parameter is set to True
'''

import re
import nltk
import string
from nltk import pos_tag, word_tokenize
from keyfrequencydictionary import *
class NGram:
    def __init__(self, text, n,throwpunctuation=False, takesentstartstop=False):
        self.noneWord = "*"
        separator = "_"
        self.nGram = []
        self.windowSize = n
        ngram = ""
        
        if not isinstance(text, list):
            text = [text]
        for sentence in text:#loop over each sentence
            if throwpunctuation:
                sentence = re.sub(r'['+string.punctuation+']+'," ",sentence)
                sentence = re.sub(r'[ ]{2,}'," ",sentence)
                
            tokens = word_tokenize(sentence)
            #-(n-1)....-3,-2,-1,0,1,2,...,len(tokens)-1
            for i in range(-(n-1), len(tokens)):#loop over each words in sentence
                ngram=""
                for k in range(0,n):
                    if (i + k) < 0 or (i + k) >=len(tokens):
                        ngram += self.noneWord + separator
                    else:
                        ngram += tokens[i+k] + separator

                if (not takesentstartstop) and self.noneWord in ngram:
                    continue
                self.nGram.append(ngram.strip(separator))
                

        self.ngramDictionary = KeyFrequencyDictionary()
        for ngrm in self.nGram:#check if start or end of sentence to consider
            if (not takesentstartstop) and self.noneWord in ngrm:
                continue
            self.ngramDictionary.addtoDictionary(ngrm.lower())
                

    def getMyList(self):
        return self.nGram

    def getMyDictionary(self):
        return self.ngramDictionary

    def getNGramGrammar(self, ngram, worddictionary, smoothing=False):

        #print(worddictionary)
        probability = 0
        ngram = ngram.lower()
        v = len(worddictionary)
        #print(v)
        cwi_1wi = 0
        cwi_1 = 0

        if ngram in self.ngramDictionary.getDictionary():
            cwi_1wi = self.ngramDictionary.getDictionary()[ngram]
            
        wi_1 = ngram.split("_")[0]
        if wi_1 in worddictionary:#if wi-1 in vocabulary
            cwi_1 = worddictionary[wi_1]
        else:
            cwi_1 = cwi_1 + 1 # handle for unknown word by counting to 1
        if smoothing:
            probability = (cwi_1wi + 1)/(cwi_1 + v)
        else:
            probability = cwi_1wi/cwi_1

        return probability

        

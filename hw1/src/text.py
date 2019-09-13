'''
Author: Dipesh Gautam
dgautam@memphis.edu
File: text.py
'''
import re
import string
class Text:
    'Class to tokenize strings in a file'
    
    def __init__(self, txt):
        self.text = txt.lower()
        self.tokens = []
        self.tokenfreqmap = {}

    def tokenize(self):
        #self.tokens=self.text.split()

        #puncts = string.punctuation
        self.tokens = re.findall( r'[a-z]+|['+string.punctuation+']', self.text, re.M|re.I)
        for token in self.tokens:
            
            i=0
            if token in self.tokenfreqmap:
                i = self.tokenfreqmap[token]

            i += 1
            self.tokenfreqmap[token] = i
        sortdict = [(v, k) for k, v in self.tokenfreqmap.items()]
        sortdict.sort()
        sortdict.reverse()
        sortdict = [(k, v) for v, k in sortdict]

        self.tokenfreqmap = sortdict
        #print(self.tokenfreqmap)
        #print(self.tokenfreqmap)

    def getCount(self,str):
        #print("test")
        return self.tokenfreqmap[str]

    def printAll(self):
        print(self.tokenfreqmap)


    def getmostFrequent(self, n):
        'returns n most frequent tokens'
        count=0
        for word in self.tokenfreqmap:
            print(word)
            count +=1
            if(count==n):
                break

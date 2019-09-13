'''
Author: Dipesh Gautam
E-Mail: dgautam@memphis.edu

This module implements Corpus class.
The Corpus class has one argument constructor;
the constructor argument is the raw corpus file
The class parses the corpus file to get clean corpus
'''
import re
import string
class Corpus:
    'Class to tokenize strings in a file'
    def __init__(self, corpusfile):
        self.corpusFile = corpusfile
        self.taggedSentences = []
    'function to parse the corpus'  
    def extractParsedSentences(self):
        'flag that is set to true when sentence ends and set to false when sentence starts until it ends'
        end = True
        'current sentence that is being scanned'
        current = ""
        for line in self.corpusFile:

            line1 = line.strip(" \r\n")
            line1 = re.sub(r'[()]+',"",line1)

            '''skip empty line'''
            if(line == ""):
                continue
            splt = line1.split(" ")
            #if splt[len(splt)-2] == "NN":
                #print(splt[len(splt)-2] + " " + splt[len(splt)-1])
            
            '''check if new sentence starts or ends from the line read
            if new sentence starts or ends append the recovered sentence to a list'''

            if (self.isSentenceEnd(splt) or self.isNextSentenceStart(splt)):
                if self.isSentenceEnd(splt):
                    end = True
                elif self.isNextSentenceStart(splt):
                     end = False
                if current != "":
                    self.taggedSentences.append(current.strip())
                    current=""       
            if not end:
                #if splt[len(splt)-2] == "NN":
                    #print(splt[len(splt)-2] + " " + splt[len(splt)-1])
                if(current != ""):
                   current += " " + splt[len(splt)-2] + " " + splt[len(splt)-1]
                else:
                    current += splt[len(splt)-2] + " " + splt[len(splt)-1]

        #append the last sentence
        if current != "":
                    self.taggedSentences.append(current.strip())
                    
        self.corpusFile.seek(0) # reset the file pointer after completing reading
        return self.taggedSentences;

    '''-------------------------------------------------------------------'''
    def isNextSentenceStart(self,ssplit):
        #line = line.strip(" ")
        if(ssplit[0]=='TOP' and ssplit[1]!='END_OF_TEXT_UNIT'):
            return True
        return False

    '''-------------------------------------------------------------------'''
    def isSentenceEnd(self,ssplit):
        #line = line.strip(" ")
        
        if(ssplit[0]=='TOP' and ssplit[1]=='END_OF_TEXT_UNIT'):
            return True
        return False

    

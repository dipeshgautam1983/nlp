'''
Author: Dipesh Gautam
e-mail: dgautam@memphis.edu

This is the main program. It consists of Output class that implements
two functions. exportWordFrequency function exports word frequency count to csv file.
printBigramGrammar prints the bigram grammar.
'''
import nltk
from nltk import pos_tag, word_tokenize
from corpus import *
from keyfrequencydictionary import *
from ngram import *
import string
class Output:
    def __init__(self, corpusfile):
        self.objCorpus = Corpus(corpusfile)
        self.sentenceList = self.objCorpus.getPureSentences()
        self.wordDictionary = KeyFrequencyDictionary()

    '''Export to csv file for Zipfs law'''
    def exportWordFrequency(self,outfile = ""):
        for sentence in self.sentenceList:
            tokens = word_tokenize(sentence)
            for token in tokens:
                if token not in string.punctuation:
                    self.wordDictionary.addtoDictionary(token.lower())
    
        sortedworddictionary = self.wordDictionary.sortByFrequency()
        if(outfile==""):
            return
        file = open(outfile,"w")
        
        for word, freq in sortedworddictionary:
            file.write(word + "," + str(freq) + "\n")
            #print(word)

        file.close()
            


    '''Print the Bigram grammar for given sentence'''
    def printBigramGrammar(self, sentence):
        
        modelbigram = NGram(self.sentenceList,2,True)#True = throw punctuations

        bigramslist = modelbigram.getMyList()
        bigram2 = NGram(sentence,2,True).getMyList()#True = throw punctuations
        #sump = 0
        print("Bigram grammar before smoothing")
        for bigram in bigram2:
            #print(bigram)
            prob =  modelbigram.getNGramGrammar(bigram,self.wordDictionary.getDictionary())
            #sump+= prob
            print(bigram, prob)
        print("\n___________________________________\nBigram grammar after smoothing")
        for bigram in bigram2:
            #print(bigram)
            prob =  modelbigram.getNGramGrammar(bigram,self.wordDictionary.getDictionary(),True) # smoothing=True
            #sump+= prob
            print(bigram, prob)


'''---------Execution starts from here-------------'''
corpusfile = "snapshotBROWN.pos.all.txt"

print("Exporting to CSV")
print("........")
output = Output(corpusfile)
output.exportWordFrequency("zipfs.csv")
print("CSV Exported\n................")
sentence = "A similar resolution passed in the Senate"
output.printBigramGrammar(sentence)


'''
Author: Dipesh Gautam
E-Mail: dgautam@memphis.edu

This module is dependent on hashesofhash.
This module uses most frequent tag returned from hashofhashes.py module for a given word 
to tag the word that occurred in other context
This module also calculates the performance of the tagger
'''
from hashofhashes import CorpusHash

import nltk
from nltk import pos_tag, word_tokenize
'This class is dependent on hashofhashes.py'
class LexicalizedStatisticalBaselineTagger:

    def __init__(self,corpusfile):
        self.corpusFile = corpusfile

        self.corpusHash = CorpusHash(self.corpusFile)
        self.corpusHash.createHashes()
        'find most frequent tag'
        #self.mostFrequentTag = self.corpusHash.getMostFrequentTag()
        
        self.statistics = {"correct":0,"incorrect":0,"total":0, "accuracy":0}

   
    '''
    def tag_text(self,textfile):
            for line in self.corpusFile:
                line1 = line.strip(" \r\n")
                splt = line1.split(" ")
                for i in range(0,len(splt),2):
                    tag = splt[i]
                    word = splt[i+1]
                    if tag == self.mostFrequentTag:
                        self.statistics["correct"] += 1
                        #pass
                    else:
                        self.statistics["incorrect"] += 1
                        #pass
                    self.statistics["total"] += 1
                
        self.corpusFile.seek(0)
    '''
    def applyRules(self,initialtags, words):
        temptags = list(initialtags)
        unknownindex = []
        #tag with most frequent tag in corpus
        for i in range(0, len(initialtags)):
            if initialtags[i] == "UNKNOWN":
                unknownindex.append(i)
                temptags[i] = self.corpusHash.getMostFrequentTag()
                #print("tag: " + temptags[i])

        #print(unknownindex)
        #apply rules from here
        for i in unknownindex:
            #print("word: ", i, words[0])
            word = words[i].lower()
            tag_0 = temptags[i]
            tag_1 = ""
            tag_2 = ""
            tag_3 = ""
            tag1 = ""
            tag2 = ""
            if i>0:
                tag_1 = temptags[i-1]
            if i>1:
                tag_2 = temptags[i-2]
            if i>2:
                tag_3 = temptags[i-3]
            if i<len(temptags)-1:
                tag1 = temptags[i+1]
            if i < len(temptags) -2:
                tag2 = temptags[i+2]

            if tag_0 == "NN" and tag_1 == "TO": #1
                tag_0 = "VB"
            if tag_0 == "VBP" and (tag_1 == "MD" or tag_2 == "MD" or tag_3 == "MD"): #2
                tag_0 = "VB"
            if tag_0 == "NN" and (tag_1 == "MD" or tag_2 == "MD"): #3
                tag_0 = "VB"
            if tag_0 == "VB" and (tag_1 == "DT" or tag_2 == "DT"): #4
                tag_0 = "NN"
            if tag_0 == "VBD" and (tag_1 == "VBZ" or tag_2 == "VBZ" or tag_3 == "VBZ"): #5
                tag_0 = "VBN"
            if tag_0 == "VBN" and tag_1 == "PRP": #6
                tag_0 = "VBD"
            if tag_0 == "VBN" and tag_1 == "NNP": #7
                tag_0 = "VBD"
            if tag_0 == "VBD" and tag_1 == "VBD": #8
                tag_0 = "VBN"
            if tag_0 == "VBP" and tag_1 == "TO": #9
                tag_0 = "VB"
            if tag_0 == "POS" and tag_1 == "PRP": #10
                tag_0 = "VBZ"
            if tag_0 == "VB" and tag_1 == "NNS": #11
                tag_0 = "VBP"
            if tag_0 == "VBD" and (tag_1 == "VBP" or tag_2 == "VBP" or tag_3 == "VBP"): #12
                tag_0 = "VBN"
            if tag_0 == "IN" and (tag1 == "VB" or tag2 == "VB"): #13
                tag_0 = "WDT"
            if tag_0 == "VBD" and (tag_1 == "VB" or tag_2 == "VB"): #14
                tag_0 = "VBN"
            if tag_0 == "VB" and tag_1 == "PRP": #15
                tag_0 = "VBP"
            if tag_0 == "IN" and tag1 == "VBZ": #16
                tag_0 = "WDT"
            if tag_0 == "IN" and tag1 == "NN": #17
                tag_0 = "DT"
            if tag_0 == "JJ" and tag1 == "NNP": #18
                tag_0 = "NNP"
            if tag_0 == "IN" and tag1 == "VBD": #19
                tag_0 = "WDT"
            if tag_0 == "JJR" and tag1 == "JJ": #20
                tag_0 = "RBR"


            if tag_0 == "NN" and word.endswith("s"): #1
                tag_0 = "NNS"
            if tag_0 == "NN" and ('.' in word): #2
                tag_0 = "CD"
            if tag_0 == "NN" and ('-' in word): #3
                tag_0 = "JJ"
            if tag_0 == "NN" and word.endswith("ed"): #4
                tag_0 = "VBN"
            if tag_0 == "NN" and word.endswith("ing"): #5
                tag_0 = "VBG"
            if word.endswith("ly"): #6
                tag_0 = "RB"
            #if tag_0 == "NN" and tag_1 == "NNS": #7
                #tag_0 = "VB"
            #if tag_0 == "NN" and tag_1 == "CD": #8
                #tag_0 = "VB"
            if tag_0 == "NN" and  word.endswith("al"): #9
                tag_0 = "JJ"
            #if tag_0 == "NN" and tag_1 == "CD": #10
                #tag_0 = "VB"
            if tag_0 == "NN" and any(char.isdigit() for char in word): #11
                tag_0 = "CD"
            #if tag_0 == "NN" and tag_1 == "CD": #12
                #tag_0 = "VB"
            if tag_0 == "NNS" and  word.endswith("us"): #13
                tag_0 = "JJ"
            #if tag_0 == "NN" and tag_1 == "CD": #14
                #tag_0 = "VB"
            if tag_0 == "NN" and  word.endswith("ble"): #15
                tag_0 = "JJ"
            if tag_0 == "NN" and  word.endswith("ic"): #16
                tag_0 = "JJ"
            #if tag_0 == "NN" and tag_1 == "NNS": #17
                #tag_0 = "VB"
            if tag_0 == "NNS" and  word.endswith("ss"): #18
                tag_0 = "NN"
            #if tag_0 == "NN" and tag_1 == "CD": #19
                #tag_0 = "VB"
            if tag_0 == "NN" and  word.endswith("ive"):#20
                tag_0 = "JJ"

            temptags[i] = tag_0
        return temptags
        
    def tagSentence(self, sentence,userule=False):

        sentence = sentence.strip(" \r\n")
        splt = word_tokenize(sentence)
        #splt = sentence.split(" ")
        initialtags = [];
        words = []
        for word in splt:
            #word = word.lower()
            if self.corpusHash.hasWord(word):
                tag = self.corpusHash.getMostLikeliTag(word)
            else:
                #print("UNKNOWN")
                tag = "UNKNOWN"
            initialtags.append(tag)
            words.append(word)

        tags=[]
        if userule:
            tags = self.applyRules(initialtags,words)
        else:
            tags = initialtags
        #tags = initialtags
        #reconstruct the tagged sentence
        tagged_sentence = ""
        for i in range(0, len(words)):
            if i==0:
                tagged_sentence += (tags[i] + " " + words[i])
            else:
                tagged_sentence += " " + (tags[i] + " " + words[i])

        return tagged_sentence
        

    def tagRawText(self, inpfile, outpfile,userule=False):
        infile = open(inpfile)
        outfile = open(outpfile,"w")
        firstline = True
        for line in infile:
            line1 = line.strip(" \r\n")
            tagged = self.tagSentence(line1,userule)
            if not firstline:
                outfile.write("\n" + tagged)
            else:
                outfile.write(tagged)
                firstline = False
        infile.close()
        outfile.close()

    def compareWithGold(self, testfile, goldfile):
        for line in testfile:
            line = line.strip(" \r\n")
            splt = line.split(" ")

            goldline = goldfile.readline().strip(" \r\n")
            goldsplt = goldline.split(" ")

            for i in range(0,len(splt),2):
                tag = splt[i]
                goldtag = goldsplt[i]
                if(tag == goldtag):
                    self.statistics["correct"] +=1
                else:
                    self.statistics["incorrect"] +=1
                self.statistics["total"] += 1
        self.statistics["accuracy"] = 100 * self.statistics["correct"]/self.statistics["total"]
        
    def computePerformanceStatistics(self,tstfile, gldfile=None):

        self.statistics = {"correct":0,"incorrect":0,"total":0, "accuracy":0}
        
        testfile = open(tstfile)
        if gldfile !=None:
            goldfile = open(gldfile)
            self.compareWithGold(testfile,goldfile)
            testfile.close()
            goldfile.close()
            return self.statistics

        
        
        for line in testfile:
            line1 = line.strip(" \r\n")
            splt = line1.split(" ")
            for i in range(0,len(splt),2):
                tag = splt[i]
                word = splt[i+1]
                word = word.lower()
                #print("word: " + self.corpusHash.getMostLikeliTag(word))
                if(tag != "-NONE-"):
                    if tag == self.corpusHash.getMostLikeliTag(word):
                        self.statistics["correct"] += 1
                        #pass
                    else:
                        self.statistics["incorrect"] += 1
                        #pass
                    self.statistics["total"] += 1
                
        #testfile.seek(0)
        testfile.close()
        self.statistics["accuracy"] = 100 * self.statistics["correct"]/self.statistics["total"]
        return self.statistics
        

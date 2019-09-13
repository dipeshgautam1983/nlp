'''
Author: Dipesh Gautam
E-Mail: dgautam@memphis.edu

This module is dependent on hashesofhash.
This module finds most frequent tags from the Tag Hash returned
from hashesofhash module and use the most frequent tag to tag all
the words in the corpus.
This module also calculates the performance of the tagger
'''
from hashofhashes import CorpusHash
'This class is dependent on hashofhashes.py'
class StatistaticalBaselineTagger:

    def __init__(self,corpusfile):
        self.corpusFile = corpusfile

        self.corpusHash = CorpusHash(self.corpusFile)
        self.corpusHash.createHashes()
        'find most frequent tag'
        for tag, freq in self.corpusHash.getTagHash():
            self.mostFrequentTag = tag
            break
        self.statistics = {"correct":0,"incorrect":0,"total":0, "accuracy":0}

    def getMostFrequentTag(self):
        
        return self.mostFrequentTag

    def computePerformanceStatistics(self):

        
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
        self.statistics["accuracy"] = 100 * self.statistics["correct"]/self.statistics["total"]
        return self.statistics
        

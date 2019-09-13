'''
Author: Dipesh Gautam
E-Mail: dgautam@memphis.edu

This is the main file from where the program starts execution
'''
from corpus import *
from hashofhashes import *
from tagger import *

#clean the corpus
file = open("SnapshotBROWN.pos.all.txt")
corpus = Corpus(file)
sent = corpus.extractParsedSentences()
file.close()
print("\nSaving the clean corpus:\n")
#save the clean corpus
opfile = open("BROWN-clean.pos.txt","w")
for s in sent:
    #print(s)
    opfile.write(s + "\n")
opfile.close()
print("\nClean corpus saved:\n")
#create hash of hashes
cleanfile = open("BROWN-clean.pos.txt")
hashofhash = CorpusHash(cleanfile)
hashofhash.createHashes()
cleanfile.close()

#print hash of hashes
print("\nHash of hashes:\n")
print(hashofhash.getHashOfHashes())

#print 20 most frequent tags
print("\n20 most frequent tags:\n")

print(hashofhash.getmostFrequentTags(20))
#tag the words with most frequent tags
cleanfile1 = open("BROWN-clean.pos.txt")
tagger = StatistaticalBaselineTagger(cleanfile1)

#print the performance
print("\nPerformance of Tagger: \n")
print(tagger.computePerformanceStatistics())
cleanfile1.close()


'''
Author: Dipesh Gautam
E-Mail: dgautam@memphis.edu

This is the main file from where the program starts execution
'''
from corpus import *
from hashofhashes import *
from lixicalizedstatisticaltagger import *

#clean the corpus
file = "BROWN.pos.all"
corpus = Corpus(file)
sent = corpus.extractParsedSentences()

print("\nSaving the clean corpus:\n")
#save the clean corpus
opfile = open("cleanBROWN.pos.all.txt","w")
for s in sent:
    #print(s)
    opfile.write(s + "\n")
opfile.close()
print("\nClean corpus saved:\n")

#Train the tagger with all the Clean Brown corpus
print("Training the tagger")
trainingfile = "cleanBROWN.pos.all.txt"
tagger = LexicalizedStatisticalBaselineTagger(trainingfile)

#Test the tagger with clean Brown Snapshot corpus
testfile = "snapshotBROWN-clean.pos.txt"
#print the performance
print("\nPerformance of the tagger for tagging Brown Snapshot corpus: \n")
print(tagger.computePerformanceStatistics(testfile))

#Tag the raw text file
print("\n25 news sentences tagging")
myrawtextfile = "news_25_sentences.txt"
mytagged = "my_25tagged_file.txt"
mygoldtagged = "news_25_tagged_sentences.txt"

tagger.tagRawText(myrawtextfile,mytagged,False)#use rule = False
print("\nPerformance for tagging 25 news sentences without rules")
print(tagger.computePerformanceStatistics(mytagged,mygoldtagged))

tagger.tagRawText(myrawtextfile,mytagged,True)#use rule = True
print("\nPerformance for tagging 25 news sentences with rules")
print(tagger.computePerformanceStatistics(mytagged,mygoldtagged))




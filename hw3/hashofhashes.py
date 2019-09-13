'''
Author: Dipesh Gautam
E-Mail: dgautam@memphis.edu

This module consists of CorpusHash which has one argument constructor;
and the argument is the clean corpus file that has only word and tag.
'''
class CorpusHash:
    'class to create hash of hash from corpus'
    def __init__(self, corpusfile):
        self.corpusFile = open(corpusfile)
        self.hashOfHashes = {}
        self.tagHash = {}
    def __del__(self):
        self.corpusFile.close()

    def createHashes(self):
        #print("hi")
        for line in self.corpusFile:
            
            line1 = line.strip(" \r\n")
            #print(line1)
            splt = line1.split(" ")
            for i in range(0,len(splt),2):
                tag = splt[i]
                word = splt[i+1]
                word = word.lower()
                #print(tag + " " + word)
                self.insertInHashOfHashes(word,tag)
                self.insertInTagHash(tag)

        self.corpusFile.seek(0)
        self.tagHash = self.sortHashByFrequency(self.tagHash)
        #self.sortTagHashByFrequency()
        '''sort each hash in hash of hashes'''
        for key in self.hashOfHashes:
            temphash = self.hashOfHashes[key]
            self.hashOfHashes[key] = self.sortHashByFrequency(temphash)
                

    def insertInTagHash(self, tag):
        i = 0
        if tag in self.tagHash:
            i = self.tagHash[tag]
        i += 1
        self.tagHash[tag] = i

    def sortHashByFrequency(self,myhash):

        sortdict = [(v, k) for k, v in myhash.items()]
        sortdict.sort()
        sortdict.reverse()
        sortdict = [(k, v) for v, k in sortdict]

        return sortdict
        

    '''
    def sortTagHashByFrequency(self):

        
        sortdict = [(v, k) for k, v in self.tagHash.items()]
        sortdict.sort()
        sortdict.reverse()
        sortdict = [(k, v) for v, k in sortdict]

        self.tagHash = sortdict
        
        self.tagHash = self.sortHashByFrequency(self.tagHash)
    '''

    def insertInHashOfHashes(self,word, tag):

        myhash = {}
        i = 0
        word = word.lower()
        if word in self.hashOfHashes:
            myhash = self.hashOfHashes[word]
            if tag in myhash:
                i = myhash[tag]

        i += 1
        myhash[tag] = i
        self.hashOfHashes[word] = myhash
            
    def getHashOfHashes(self):
        return self.hashOfHashes

    def getHashOfWord(self, word):
        word = word.lower()
        return self.hashOfHashes(word)

    def getTagHash(self):
        return self.tagHash

    def hasWord(self,word):
        return (word.lower() in self.hashOfHashes)

    def getMostFrequentTags(self, n):
        'returns n most frequent tokens'
        count=0
        rethash = {}
        for tag, freq in self.tagHash:
            #print(word)
            rethash[tag] = freq
            count +=1
            if(count==n):
                break

        sortdict = [(v, k) for k, v in rethash.items()]
        sortdict.sort()
        sortdict.reverse()
        sortdict = [(k, v) for v, k in sortdict]

        rethash = sortdict
        return rethash

    def getMostFrequentTag(self):
        for tag, freq in self.tagHash:
            return tag
        
    
    def getMostLikeliTag(self,word):
        word = word.lower()
        temphash = self.hashOfHashes[word]
        for tag, freq in temphash:
            return tag
        

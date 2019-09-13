'''
Author: Dipesh Gautam
E-Mail: dgautam@memphis.edu

This module extracts grammar rules from a corpus (Brown corpus)
The input to the constructor is the path of Brown corpus
'''

import re
import string
class RuleExtractor:
    
    def __init__(self, corpusfile):
        
        self.corpusFile = open(corpusfile)
        self.myRules = {}
        self.myUniqueRules = {}
        self.mySortedUniqueRules = {}
        self.myParents = {}
        self.myNodes = []
    def __del__(self):
        self.corpusFile.close()

    def extractRules(self):
    
        parent = -1
        currentnode = -1
        leafencountered = False
        for line in self.corpusFile:
            
            line = line.strip(" \r\n")
            if(line=="" or line == "(TOP END_OF_TEXT_UNIT)"):
                continue
            line = re.sub(r'[(]'," ( ",line)
            line = re.sub(r'[)]',") ",line)
            line = re.sub(r'[ ]+'," ",line)
            line = line.strip()

            pushmode = False
            splits = line.split(" ")
            
            for splt in splits:
                if(splt=="("):
                    pushmode = True
                #if at leaf
                if(")" in splt):
                    pushmode = False
                    leafencountered = True
                    if(splt.strip() == ")"):
                        parent = self.myParents[parent] #parent of parent

                if(pushmode and splt!="("):
                    if(leafencountered):
                        leafencountered = False
                        pass
                    else:
                        parent = currentnode
                    currentnode += 1
                    if parent in self.myRules:
                        children = self.myRules[parent] + " " + splt
                    else:
                        #children = str(currentnode)
                        children = splt
                    '''Store rules here'''
                    self.myNodes.append(splt)
                    self.myRules[parent] = children
                    self.myParents[currentnode] = parent
        self.createRules()

    def createRules(self):
        for nodeid in self.myRules:
            if(nodeid <= 0):
                continue
            node = self.myNodes[nodeid]
            node = re.sub( r'-[0-9]+', "", node)
            sisters = self.myRules[nodeid]
            sisters = re.sub( r'-[0-9]+', "", sisters)
            sisters = re.sub(r'['+string.punctuation+']', "", sisters).strip()
            
            if(node in string.punctuation or sisters =="" or 'TOP' in node):
                #print(node)
                continue
            
            rule = node + " -> " + sisters
            
            if(rule not in self.myUniqueRules):
                self.myUniqueRules[rule] = 1
            else:
                self.myUniqueRules[rule] = self.myUniqueRules[rule] + 1
            
            #print(node + " -> " + sisters)


    def sortDictbyFreq(self,myhash):

        sortdict = [(v, k) for k, v in myhash.items()]
        sortdict.sort()
        sortdict.reverse()
        sortdict = [(k, v) for v, k in sortdict]

        return sortdict            

    def getUniqueRules(self):
        self.mySortedUniqueRules = self.sortDictbyFreq(self.myUniqueRules)
        return self.mySortedUniqueRules

    def getMostDiverseNonTerminal(self):
        diverse = {}
        for rule, freq in self.mySortedUniqueRules:
            rule = rule.split(" -> ")[0]
            if(rule in diverse):
                diverse[rule] = diverse[rule] + 1
            else:
                diverse[rule] = 1

        return self.sortDictbyFreq(diverse)
        


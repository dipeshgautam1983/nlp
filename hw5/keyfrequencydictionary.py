'''
Author: Dipesh Gautam
e-mail: dgautam@memphis.edu

This class implements several operations on dictionary.
The important operation implemented here is sorting the
dictionary based on numeric value in key value pair; i.e frequency
'''
class KeyFrequencyDictionary:
        
    def __init__(self, keys=None):

        if keys is None:
            self.Dictionary = {}
            return
        if not isinstance(keys, list):
            raise TypeError("Keys must be of list type")
        #self.Keys = keys
        self.Dictionary = {}
        #print(self.Keys)
        for key in keys:
           self.addtoDictionary(key)
            
    def addtoDictionary(self, key):
        if key not in self.Dictionary:
            self.Dictionary[key] = 1
        self.Dictionary[key] += 1

    def getDictionary(self):
        return self.Dictionary
    def sortByFrequency(self):
        sortdict = [(v, k) for k, v in self.Dictionary.items()]
        sortdict.sort()
        sortdict.reverse()
        sortdict = [(k, v) for v, k in sortdict]
        return sortdict

    

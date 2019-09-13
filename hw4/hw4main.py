'''
Author: Dipesh Gautam
E-Mail: dgautam@memphis.edu

This module executes the rule extractor
to extract grammar rules from Brown corpus
'''


from ruleextractor import *
file = "../BROWN.pos.all"
#file = "../SnapshotBROWN.pos.all.txt"
extractor = RuleExtractor(file)
extractor.extractRules()

rules = extractor.getUniqueRules()
print("Total #distinct rules = " + str(len(rules)))

for rule in rules:
    print(rule)

diverse = extractor.getMostDiverseNonTerminal()
print("\r\nDiverse rules:\r\n")
for div in diverse:
    print(div)


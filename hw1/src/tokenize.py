'''
Author: Dipesh Gautam
dgautam@memphis.edu
File: tokenize.py
'''
from text import *

file = open("paragraph.txt")

str = file.read()
file.close()

text = Text(str)
text.tokenize()

#text.printAll()
print("The 10 most frequent words are:")
text.getmostFrequent(10)


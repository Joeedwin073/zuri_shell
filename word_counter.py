#A python program to count the number of words in a given text

from itertools import count
from posixpath import split


wordcount = input("What is the text you want to count? ")

words = wordcount.strip(" ")

counter = len(words.split())
 
print("No of words = ", counter)
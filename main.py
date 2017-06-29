#!/usr/bin/env python3

from random import choice, randint
import datetime, sys, textwrap
from time import gmtime, strftime

nouns = open('nouns.txt').read().split()
adjectives = open('adjectives.txt').read().split()
verbs = open('verbs.txt').read().split()

author ="kptn"

def header():
	print("*" * 40)
	print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	print("=" * (9 - int(len(author) / 2) + len(author) % 2) +" a poem written by ~" + author + "~ " + "=" * (9 - int(len(author) / 2)))
	print("*" * 40)
	print()

def poem(min,max):
	for x in range(randint(min,max)):
		words1 = " ".join([choice(adjectives) + ", ", choice(adjectives)])
		words2 = " ".join([choice(nouns), choice(verbs)])
		words3 = " ".join([choice(nouns), choice(nouns), choice(adjectives), choice(nouns)])

		for i in range(randint(2,5)):
			words = choice([words1, words2, words3])
			line = " "*randint(0, 40 - len(words)) + words
			print(line)
        
		if x % 3 ==0:
			print()
			print(" "*5 + choice(nouns))
			print(" "*5 + choice(nouns))
			print(" "*5 + "the " + choice(nouns) +"!")
			print()
	        
		if x % 7 ==0:
			words4 = " ".join(["the " + choice(adjectives), choice(nouns), choice(verbs)])
			print()
			s = (" ").join(words4)
			print(textwrap.fill(s , width=41))
			print()


old_stdout = sys.stdout
log_file = open("poems.txt","a")
sys.stdout = log_file

header()
poem(5,11)

sys.stdout = old_stdout
log_file.close()

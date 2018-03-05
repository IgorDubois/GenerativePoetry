#!/usr/bin/env python3

from random import choice, randint
import datetime, sys, textwrap
from time import gmtime, strftime
import argparse

def num(s):
	try:
		return int(s)
	except ValueError:
		return float(s)

def header(n, author):
	print("*" * 40)
	print("* {:5} *****".format(n) + strftime(" %c *", gmtime()))
	print("*" * (40 - len(author) - 6) + " by " + author + " *")
	print("*" * 40)
	print()

def poem(length, nouns, adjectives, verbs):
	for x in range(length):
		words1 = " ".join([choice(adjectives) + ", ", choice(adjectives)])
		words2 = " ".join([choice(nouns), choice(verbs)])
		words3 = " ".join([choice(nouns), choice(nouns), choice(adjectives), choice(nouns)])

		for i in range(randint(2,5)):
			words = choice([words1, words2, words3])
			line = ""
			if len(words) < 40:
				line = " "*randint(0, 40 - len(words)) + words
			else:
	    			line = words
			print(line)

		if x % 3 ==0:
			print()
			print(" "*5 + choice(adjectives))
			print(" "*5 + choice(verbs))
			print(" "*5 + "the " + choice(nouns) +"!")
			print()

		if x % 5 ==0:
			print()
			print(" "*1 + choice(nouns) + "y")
			verb = choice(verbs)
			if verb[-1] == "e":
    				print(" "*3 + choice(verbs)[:-1] + "ing")
			else:
					print(" "*3 + choice(verbs) + "ing")
			n = choice(nouns)
			if n[-1] == "e":
				n = n + "r"
			if n[-3:] == "ion":
				n = n[:-3] + "or"
			else:
				n = n + "er"
			print(" "*5 + "the" + ((" " + n) * randint(1,3)) +"!")
			print()

		if x % 7 ==0:
			print()
			print("the " + choice(adjectives) + " " + choice(nouns))
			print(choice(verbs)+ "s")
			print("the " + choice(adjectives) + " " + choice(nouns))
			print()

		if x % 11 ==0:
			print("~to " + choice(verbs) + " is to " + choice(verbs))
			print()

def poem_html(length, nouns, adjectives, verbs):
	print("<div class=\"poem\">")
	for x in range(length):
		words1 = " ".join([choice(adjectives) + ", ", choice(adjectives)])
		words2 = " ".join([choice(nouns), choice(verbs)])
		words3 = " ".join([choice(nouns), choice(nouns), choice(adjectives), choice(nouns)])

		for i in range(randint(2,5)):
			words = choice([words1, words2, words3])
			line = ""
			if len(words) < 40:
				line = " "*randint(0, 40 - len(words)) + words
			else:
				line = words
			line = "<p class=\"verse\">" + line + "</p>"
			print(line)

		if x % 3 ==0:
			print("<p class=\"verse3\">")
			print(choice(adjectives))
			print(choice(verbs))
			print("the " + choice(nouns) +"!")
			print("</p>")

		if x % 5 ==0:
			print("<p class=\"verse5\">")
			print(choice(nouns) + "y")
			verb = choice(verbs)
			if verb[-1] == "e":
    				print(choice(verbs)[:-1] + "ing")
			else:
					print(choice(verbs) + "ing")
			n = choice(nouns)
			if n[-1] == "e":
				n = n + "r"
			if n[-3:] == "ion":
				n = n[:-3] + "or"
			else:
				n = n + "er"
			print("the" + ((" " + n) * randint(1,3)) +"!")
			print("</p>")

		if x % 7 ==0:
			print("<p class=\"verse7\">")
			print("the " + choice(adjectives) + " " + choice(nouns))
			print(choice(verbs)+ "s")
			print("the " + choice(adjectives) + " " + choice(nouns))
			print("</p>")

		if x % 11 ==0:
			print("<p class=\"verse11\">")
			print("~to " + choice(verbs) + " is to " + choice(verbs))
			print("</p>")

	print("</div>")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("author", type=str, help="the author\'s name")
	parser.add_argument("nouns", type=str, help="the file containing the noun database. Each word must be on his line")
	parser.add_argument("adjectives", type=str, help="the file containing the adjectives database. Each word must be on his line")
	parser.add_argument("verbs", type=str, help="the file containing the verbs database. Each word must be on his line")
	parser.add_argument("output", type=str, help="the output file")
	parser.add_argument("length", type=int, help="the number of poems generated")
	args = parser.parse_args()

	nouns = open(args.nouns).read().split('\n')
	adjectives = open(args.adjectives).read().split('\n')
	verbs = open(args.verbs).read().split('\n')

	old_stdout = sys.stdout
	log_file = open(args.output,"a")
	sys.stdout = log_file

	length = int(args.length)

	for n in range(1,length):
		# header(n, args.author)
		poem_html(3, nouns, adjectives, verbs)

	sys.stdout = old_stdout
	log_file.close()

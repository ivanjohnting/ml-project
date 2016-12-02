# -*- coding: utf-8 -*-


# import re

import string


train = open('EN/train', encoding = "utf8")
test = open('EN/dev.in', encoding = "utf8")
gold = open('EN/dev.out', encoding = "utf8")


# train2 = codecs.open('EN/train', encoding = "utf8")

def preproccessing(train):

	digits = {}
	punctuation = {}
	year = {}
	for lines in train:
		line = lines.split()

		if line != []:

			word = line[0].lower()		#Lowercase words

			if word.isdigit() == True:	#Find digits 
				if int(word) >= 1800 and int(word) <= 2100: 	#Years
					year[word] = 1
				else:
					digits[word] = 1 			#digits 		#Can split further to phone number? dates?! how
			elif word in string.punctuation: #Find punctuations
				punctuation[word] = 1



	return digits,punctuation,year

digits,punctuation,year = preproccessing(train)
print(digits,"\n",punctuation,"\n",year)

# Was thinking. We should read each line first then sort to entities. Not by words.

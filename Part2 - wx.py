import re
from collections import Counter
from collections import namedtuple
from operator import itemgetter

train = open('EN/train', encoding = "utf8")
test = open('EN/dev.in', encoding = "utf8")
gold = open('EN/dev.out', encoding = "utf8")


def training_emission(train):
	train_xlist=[]
	train_ylist=[]
	train_xylist=[]

	for lines in train:
		line = lines.split()
		# print (line)

		if line != []:
			train_xlist.append(line[0])
			train_ylist.append(line[1])
			train_xylist.append(line)

	train_xcount = Counter(train_xlist)
	train_ycount = Counter(train_ylist)
	train_xycount = Counter(tuple(i) for i in train_xylist)
	# print (train_xcount)
	# print (train_ycount)
	# print(train_xycount)


	##### PRIOR #########
	for y in train_ycount:
		train_ycount[y] += 1
		train_xycount[("UNK123!@#",y)] = 1 		#for all unknown words have the same probability

	##### PRIOR #########


	return train_xcount,train_ycount,train_xycount


train_xcount,train_ycount,train_xycount = training_emission(train)


f = open('test.txt', 'w')
data = str(train_xycount)
f.write(data)



def emission(train_xycount,train_ycount):

	emissiondict = {}
	for key in train_xycount:
		emission = train_xycount[key]/train_ycount[key[1]]
		emissiondict[key] = emission
	return (emissiondict)

# emissiondict = emission(train_xycount,train_ycount)


# print(emissiondict)





################# Getting Rec and Rec - START  #################

# y_star = []
# list1 = []

# count = 0
# count1 = 0

# for y in train_ycount:
# 	list1.append(emissiondict[("UNK123!@#",y)])
# Unk = max(list1)

# for words in test:
# 	x = words.split()

# 	if x != []:
# 		list1 = []
# 		count += 1

# 		for key,value in emissiondict:
# 			if x == key:
# 				list1.append(emissiondict[(key,value)])
# 				count1 += 1

# 		if list1 == []:
# 			list1 =[Unk]

# 		y_star.append(max(list1))

# print(count,count1)
# print(y_star)
# print(len(y_star))
# print(len(emissiondict))


################# Getting Rec and Rec - END  #################




################ NOT SURE ##################

# test.seek(0)

# predicted_entities=[]

# for words in test:
# 	findmax=[]
# 	x = words.split()
# 	if x!=[]:
#   		for key in emissiondict:
#   			if x[0] == key[0]:
#   				findmax.append((key[1],emissiondict[key]))
#   		ystar = max(findmax,key=itemgetter(1))[0]
#   		predicted_entities.append(ystar)

# total_predicted_entities = len(predicted_entities)


# print(emissiondict)


# if x[0] not in train_xcount:
#     emiss = emissiondict[("UNK123!@#",y)]
    
  		
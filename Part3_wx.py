import re
from collections import Counter
from collections import namedtuple
from operator import itemgetter

train = open('EN/train', encoding = "utf8")
test = open('EN/dev.in', encoding = "utf8")
gold = open('EN/dev.out', encoding = "utf8")

def training_trasmission(train):
	start = 'START123'
	end = 'END123'

	train_xlist=[]
	train_ylist=[start] 			#initialize
	train_xylist=[]
	train_yylist=[]


	for lines in train:
		line = lines.split()
		# print (line)

		if line != []:
			train_xlist.append(line[0])
			train_ylist.append(line[1])
			train_xylist.append(line) 
			train_yylist.append(train_ylist[-2:])
		else:
			train_ylist.append(end)
			train_yylist.append(train_ylist[-2:])
			train_ylist.append(start)
			

	del train_ylist[-1]


	train_xcount = Counter(train_xlist)
	train_ycount = Counter(train_ylist)
	train_xycount = Counter(tuple(i) for i in train_xylist)
	train_yycount = Counter(tuple(i) for i in train_yylist)


	##### PRIOR #########
	for y in train_ycount:
		train_ycount[y] += 1
		train_xycount[("UNK123!@#",y)] = 1 		#for all unknown words have the same probability

	##### PRIOR #########

	# print (train_xcount)
	# print (train_ycount)
	# print(train_xycount)



	return train_xcount,train_ycount,train_xycount,train_yycount


# train_xcount,train_ycount,train_xycount,train_yycount = training_trasmission(train)


# print(len(train_yycount),train_yycount)



def transmission(train_ycount,train_yycount):

	transmission_dict = {}

	# #initialize
	for i in train_ycount:
		for j in train_ycount:
			transmission_dict[(i,j)] = 0

	for (key,value) in train_yycount:
		trans = train_yycount[(key,value)]/train_ycount[key]
		transmission_dict[(key,value)] = trans
	return (transmission_dict)



# transmission_dict = transmission(train_ycount,train_yycount)


# print(transmission_dict)


# counting = {}
# testing = {}
# for i,j in transmission_dict:
# 	if i not in testing:
# 		testing[i] = transmission_dict[i,j]
# 	else:
# 		testing[i] += transmission_dict[i,j]


# print(testing)





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






def emission(train_xycount,train_ycount):

	emissiondict = {}
	for key in train_xycount:
		emission = train_xycount[key]/train_ycount[key[1]]
		emissiondict[key] = emission
	return (emissiondict)

emissiondict = emission(train_xycount,train_ycount)



f = open('test.txt', 'w')
data = str(emissiondict)
f.write(data)



################# Getting Rec and Rec - START  #################

y_star = []
list1 = []
list2 = []

count = 0
count1 = 0
count2 = 0

for y in train_ycount:
	list1.append(emissiondict[("UNK123!@#",y)])
	list2.append(y)

pos = list1.index(max(list1))
yy_unk = list2[pos]


for words in test:
	x = words.split()

	if x != []:

		list1 = []
		list2 = []

		for key,value in emissiondict:
			if x[0] == key:
				prob = emissiondict[(key,value)]
				list1.append(prob)
				list2.append([key,value])
				count += 1		

		if list1 == []:
			yy = yy_unk
			count1 += 1
		else:
			pos = list1.index(max(list1))
			yy = list2[pos][1]
			count2 += 1

		y_star.append(yy)


gold_label = []
count4 = 0

for words in gold:
	x = words.split()

	if x != []:
		yy = x[1]
		gold_label.append(yy)
		if yy != 'O':
			count4 += 1


right_set = set(y_star) & set(gold_label)
right = len(right_set)
print(right)


print(count,count1,count2)
print(y_star)
print(len(y_star))

print(count1+count2,len(gold_label))


# from evalResult import get_predicted


recall = right/count2
print('recall',recall)

prec = right/count4
print('prec',prec)

F = 2/( (1/recall)+(1/prec))
print('F',F)


################# Getting Rec and Rec - END  #################

    
  		
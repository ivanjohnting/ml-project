import re
from collections import Counter
from collections import namedtuple

train = open('train', encoding = "utf8")

train_xlist=[]
train_ylist=[]
train_xylist=[]
for lines in train:
	line=lines.split()
	#print (line)
	if line!=[]:
		train_xlist.append(line[0])
		train_ylist.append(line[1])
		train_xylist.append(line)
train_xcount = Counter(train_xlist)
train_ycount = Counter(train_ylist)
train_xycount = Counter(tuple(i) for i in train_xylist)
# print (train_xcount)
# print (train_ycount)
# print(train_xycount)

emissiondict = {}
for key in train_xycount:
	emission = train_xycount[key]/train_ycount[key[1]]
	emissiondict[key] = emission
#print (emissiondict)

test = open('dev.in', encoding = "utf8")

# for lines in test:
# 	line=lines.split()
#	print (line)
# 	if line!=[]:
# 		if line[0] not in train_xcount:
# 			emission = 1/




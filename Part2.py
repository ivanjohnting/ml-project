import re
from collections import Counter
from collections import namedtuple

train = open('EN/train', encoding = "utf8")

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

#def emission(train_xycount,train_ycount):

emissiondict = {}
for key in train_xycount:
	emission = train_xycount[key]/train_ycount[key[1]]
	emissiondict[key] = emission
print (emissiondict)
#return (emissiondict)

#print (emission(train_xycount,train_ycount))

test = open('EN/dev.in', encoding = "utf8")

for words in test: 	
  	x=words.split()
  	if x!=[]:
  		if x[0] not in train_xcount:
  			for y in train_ycount:
  				emission = 1/(train_ycount[y]+1)
  				train_ycount[y] += 1
  				emissiondict[(x[0],y)] = emission
  		if x[0] in train_xcount:
  			for key in train_xycount:
  				if x[0]==key[0]:
  					emission = train_xycount[key]/(train_ycount[key[1]]+1)
  					emissiondict[key] = emission
  					
print (emissiondict)

# a={('1','2'):424}

# b='1'

# for key in a:
# 	print (key[1])
# 	if b==key[0]:
#  		print (b)



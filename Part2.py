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
print (train_ycount)
# print(train_xycount)

def emission(train_xycount,train_ycount):

	emissiondict = {}
	for key in train_xycount:
		emission = train_xycount[key]/train_ycount[key[1]]
		emissiondict[key] = emission
	return (emissiondict)

emissiondict = emission(train_xycount,train_ycount)

test = open('EN/dev.in', encoding = "utf8")

for words in test: 	
  	x=words.split()
  	if line!=[]:
  		if line[0] not in train_xcount:
  			for y in train_ycount:
  				emission = 1/(train_ycount[y]+1)
  				train_ycount[y] += 1
  				emissiondict[(x,y)] = emission
  		if line[0] in train_xcount:
  			

#print emissiondict[('ivan','testing')]


for y in train_ycount:
	train_ycount[y]+=1

print (train_ycount)

# a={(',','O'):424}

# print (a[(',','O')])
# for k1,k2 in a:
# 	print (k2)

#a=('1','2')
#print (a[0])


#"Hello testing number 2"


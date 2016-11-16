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



for y in train_ycount:
	train_ycount[y] += 1
	train_xycount[("UNK123!@#",y)] = 1 		#for all unknown words have the same probability


def emission(train_xycount,train_ycount):

	emissiondict = {}
	for key in train_xycount:
		emission = train_xycount[key]/train_ycount[key[1]]
		emissiondict[key] = emission
	return (emissiondict)

emissiondict = emission(train_xycount,train_ycount)


test = open('EN/dev.in', encoding = "utf8")



# if x[0] not in train_xcount:
#     emiss = emissiondict[("UNK123!@#",y)]
    
  			

#print emissiondict[('ivan','testing')]



# a={(',','O'):424}

# print (a[(',','O')])
# for k1,k2 in a:
# 	print (k2)

#a=('1','2')
#print (a[0])


#"Hello testing number 2"


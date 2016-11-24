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
		else:
			train_ylist.append(end)
			train_ylist.append(start)

		train_yylist.append(train_ylist[-2:])

	del train_ylist[-1]
	del train_yylist[-1]
	train_yylist.append(train_ylist[-2:])

	train_xcount = Counter(train_xlist)
	train_ycount = Counter(train_ylist)
	train_xycount = Counter(tuple(i) for i in train_xylist)
	train_yycount = Counter(tuple(i) for i in train_yylist)

	del train_yycount[(end,start)]

	# print (train_xcount)
	# print (train_ycount)
	# print(train_xycount)


	##### PRIOR #########
	for y in train_ycount:
		train_ycount[y] += 1
		train_xycount[("UNK123!@#",y)] = 1 		#for all unknown words have the same probability

	##### PRIOR #########

	print(len(train_ycount))

	return train_xcount,train_ycount,train_xycount,train_yycount


train_xcount,train_ycount,train_xycount,train_yycount = training_trasmission(train)





def transmission(train_ycount,train_yycount):

	transmission_dict = {}
	for (key,value) in train_yycount:
		trans = train_yycount[(key,value)]/train_ycount[key]
		transmission_dict[(key,value)] = trans
	return (transmission_dict)



transmission_dict = transmission(train_ycount,train_yycount)




f = open('test.txt', 'w')
# data = str(train_yycount)
data = str(transmission_dict)
f.write(data)



counting = {}
testing = {}
for i,j in transmission_dict:
	if i not in testing:
		testing[i] = transmission_dict[i,j]
	else:
		testing[i] += transmission_dict[i,j]


print(testing)

print(train_ycount['START123'],train_ycount['END123'])



counting = {}

for key in train_yycount:
	if key[0] not in counting:
		trans = train_yycount[key]
		
	else:
		trans += train_yycount[key]
	counting[key[0]] = trans

print(counting)

summ = 0
for i in counting:
	summ += counting[i]

print(summ)
print(train_ycount)



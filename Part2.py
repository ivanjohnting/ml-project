import re
from collections import Counter
from collections import namedtuple
from operator import itemgetter

train = open('EN/train', encoding = "utf8")
test = open('EN/dev.in', encoding = "utf8")
gold = open('EN/dev.out', encoding = "utf8")

####=============Estimate Emission Parameters from Training Set================###

train_xlist=[]
train_ylist=[]
train_xylist=[]
for lines in train:
	line=lines.split()
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

#return (emissiondict)

####=============Modified Emission Parameters================###

for words in test: 	
  	x=words.split()
  	if x!=[]:
  		if x[0] not in train_xcount:
  			for y in train_ycount:
  				emission = 1/(train_ycount[y]+1)
  				emissiondict[(x[0],y)] = emission
  		if x[0] in train_xcount:
  			for key in train_xycount:
  				if x[0] == key[0]:
  					emission = train_xycount[key]/(train_ycount[key[1]]+1)
  					emissiondict[key] = emission

####=============Simple sentiment analysis system================###

test.seek(0)

predicted_entities=[]
>>>>>>> 17a64792920922ae8aa6b82e512643c43710e64b

for words in test:
	findmax=[]
	x=words.split()
	if x!=[]:
  		for key in emissiondict:
  			if x[0] == key[0]:
  				findmax.append((key[1],emissiondict[key]))
  		ystar = max(findmax,key=itemgetter(1))[0]
  		predicted_entities.append(ystar)

total_predicted_entities = len(predicted_entities)

####=============Scoring================###

gold_entities = []

for lines in gold:
	line = lines.split()
	if line!=[]:
		gold_entities.append(line[1])

total_gold_entities = len(gold_entities)

total_correct_predictions = 0

for prediction in predicted_entities:
	    if prediction == gold_entities[predicted_entities.index(prediction)]:
	    	total_correct_predictions += 1


precision = total_correct_predictions/total_predicted_entities
print ('Precision = %f' % (precision))

recall = total_correct_predictions/total_gold_entities
print ('Recall = %f' % (recall))

F = 2/(1/precision + 1/recall)
print ('F score = %f' % (F))



import re
from collections import Counter
from collections import namedtuple
from operator import itemgetter

from Part2_wx import training_emission
from Part2_wx import emission
from Part3_wx import training_trasmission
from Part3_wx import transmission


train = open('EN/train', encoding = "utf8")
test = open('EN/dev.in', encoding = "utf8")
gold = open('EN/dev.out', encoding = "utf8")


train_xcount,train_ycount,train_xycount,train_yycount = training_trasmission(train)
transmission_dict = transmission(train_ycount,train_yycount)

train.close()
train = open('EN/train', encoding = "utf8")

train_xcount,train_ycount,train_xycount = training_emission(train)
emission_dict = emission(train_xycount,train_ycount)

train.close()


# print(emission_dict)
# print(transmission_dict)

# print(train_ycount)




def viterbi(emission_dict,transmission_dict,train_ycount,test):
	y_star = ""

	start = 'START123'
	end = 'END123'
	unk = "UNK123!@#"


	list1 = []
	list2 = []

	current_state = {}

	for y in train_ycount:
		list1.append(emission_dict[("UNK123!@#",y)])
		list2.append(y)
		current_state[y] = 1		

	# start_state = current_state


	order = []
	order = sorted(train_ycount.keys())
	order.reverse()
	# print(order)

	# order = ["O","B-neutral","B-positive","B-negative","I-neutral","I-positive","I-negative"]


	pos = list1.index(max(list1))
	unseen = list1[pos]


	first_state = []
	for i in range(len(order)):
		first_state.append(1)

	path = [first_state]

	path_state = []
	word_list = []


	entire_path = []


	for words in test:
		x = words.split()

		tempt_path = path[-1:][0]
		i = 0

		b = 0

		if x != []:
			# tempt_path = path[-1:]

			# i = 0
			list3 = []
			list4 = []

			word_list.append(x[0])

			for next_state in order:
				
				tempt_score=[]

				i = 0

				try:
					b = emission_dict[(x[0],next_state)]

				except Exception:
					# b = emission_dict["UNK123!@#",next_state]
					b = unseen


				for from_state in order:		

					a = transmission_dict[(from_state,next_state)]

					tempt_score.append(tempt_path[i] * a*b)
					i += 1

				pos = tempt_score.index(max(tempt_score))
				list4.append(max(tempt_score))
				list3.append(order[pos])



			path_state.append(list3)
			path.append(list4)

		else:
			i = 0
			list4 = []

			for next_state in order:
				a = transmission_dict[(next_state,end)]
				list4.append(tempt_path[i] * a)
				i += 1

			# path.append(list4)

			y_list	= []

			pos = list4.index(max(list4))
			y_list.append(order[pos])

			for i in range(len(path_state)-1,0,-1):
				y = path_state[i][pos]
				pos = order.index(y)

				y_list.append(y)

			y_list.reverse()

			# print(y_list)

			for i in range(len(y_list)):

				y_star += word_list[i] + " " +  y_list[i] + "\n"
				# y_star +=  y_list[i] + "\n"

			entire_path.append(list4)
			path = [first_state]

			path_state = []
			word_list = []

			y_star += "\n"


	return y_star,entire_path


y_star,entire_path = viterbi(emission_dict,transmission_dict,train_ycount,test)



f = open('test.txt', 'w',encoding = "utf8")
data = str(entire_path[0:10])
f.write(data)
f.close()


# for i in entire_path:
# 	print(len(i))


f = open('viterbi.out', 'w',encoding = "utf8")
data = str(y_star)
f.write(data)
f.close()



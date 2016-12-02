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
	y_star = []

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

	start_state = current_state


	order = []
	order = sorted(train_ycount.keys())
	order.reverse()
	print(order)


	pos = list1.index(max(list1))
	unseen = list1[pos]



	y_i = start

	path = []

	for words in test:
		x = words.split()

		if x != []:		

			current_state = []
			
			if y_i == start:
				for next_state in order:
					try:
						b = emission_dict[(x,next_state)]
					except Exception:
						b = unseen

					a = transmission_dict[(start,next_state)]
					
					current_state.append(a*b)

				print(current_state)
				# path.append(current_state)

			else:
				next_state = {}
				for i,pi in current_state: 		# j to i state, where i is next state 
					# tempt_state = current_state

					# pi = current_state[i]

					try:
						b = emission_dict[(x,i)]
					except Exception:
						b = unseen

					for j in train_ycount:
						list1 = []
						list2 = []

						list1.append(j)
						a = transmission_dict[(j,i)]
						list2.append(pi*a*b)

					pos = list2.index(max(list2))

					best_prev = list1[pos]		#best prev state for i state

					next_state[i] = list2[pos]

				current_state = next_state

				# path.append()



		else: 	#Do End then Initialize
			list2 = []
			for i in current_state:
				a = transmission_dict[i,end]
				list1.append(i)
				list2.append(current_state[i] * a)

			pos = list2.index(max(list2))
			best_prev = list1[pos]		##best prev state for end state


			current_state = start_state
			
			



	return y_star


y_star = viterbi(emission_dict,transmission_dict,train_ycount,test)




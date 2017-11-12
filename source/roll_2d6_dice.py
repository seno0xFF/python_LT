# coding: utf-8
import random

#5000 milion
power = pow(10,6)
five_mil = power * 5

#fumble or critilcal or norm_count init
fumb_count = 0
crit_count = 0
norm_count = 0
#total_roll = norm_count + crit_count + fumb_count

print("")
print("2dice roll start!")

#roll the dice while 100
i = 1
for i in xrange(five_mil):

#2d6 dice
	a_dice = random.randint(1,6)
	b_dice = random.randint(1,6)

### debug ###
#	print("dice1:" + str(a_dice))
#	print("dice2:" + str(b_dice))

	sum_dice = a_dice + b_dice


#roll of judge
	if sum_dice == 2:
### debug ###
#		print("Dice 2d6:" + str(sum_dice) + " Oops. This is Fumble...")
		fumb_count = fumb_count + 1
	elif sum_dice == 12:
### debug ###
#		print("Dice 2d6:" + str(sum_dice) + " Congrats! This is Critical Hit!")
		crit_count = crit_count + 1
	else:
### debug ###
#		print("Dice 2d6:" + str(sum_dice))
		norm_count = norm_count + 1
#	print("roll count: " + str(i))
	i = i + 1

### debug ###
#print("last: " + str(i))

total_roll = norm_count + crit_count + fumb_count

print("")
print("Result!!!")
print("Critical[dice6,6]: " + str(crit_count))
print("Fumble[dice1,1]: " + str(fumb_count))
print("normal[other result]: " + str(norm_count))
print("total roll: " + str(total_roll))
print("")

#want function
#fumble parcent and critical parent cariluration
#now rolling in the way Every million

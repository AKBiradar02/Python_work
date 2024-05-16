
# Interaction between python function

# how to shuffle a random list in python

example = [1,2,3,4,5,6,7]

from random import shuffle
shuffle(example)
print(example)

print('\n')

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)

print('\n')

mylist = ['','0','']

def palyer_guess():

    guess = ''

    while guess not in ['0','1','2']:
        guess = input("pick a number: 0,1 or 2")

    return int(guess)
myindex = palyer_guess()

print(myindex)

print('\n')

def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print("correct!")
    else:
        print("Wrong guess")

        print(mylist)

#Initial List
mylist = ['','0','']

#Shuffle list
mixedup_list = shuffle_list(mylist)

#User guess
guess = palyer_guess()

#Check guess
check_guess(mixedup_list,guess)


























#https://redd.it/3qjnil

from random import randint, sample
fp=open("enable1.txt", "r")
linesv2=[]
correct=0
lines=fp.read().upper()
lines=lines.split()
l=randint(4, 15)
for i in range(len(lines)):
    if len(lines[i])==int(l):
        linesv2.append(lines[i])
linesv2 = sample(linesv2, 4*int(input("Difficulty (1-5)? ")))
if len(linesv2)==20:
    [linesv2.pop() for i in range(5)]
    guesses=3
else: guesses=4
[print(i) for i in linesv2]
linesv2=''.join(sample(linesv2, 1))
while True:
    word = input("Guess (%i left)? " % guesses)
    guesses-=1
    correct=0
    for i in range(len(linesv2)):
        if word[i].lower()==linesv2[i].lower(): correct+=1
    print("{}/{} correct".format(correct, len(linesv2)))
    if word.lower()==linesv2.lower(): print("You win!"); break
    elif guesses==0: print("GAME OVER!\nThe Word Was: %s" % linesv2); break

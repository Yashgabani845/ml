import random
computer= random.choice([1,2,3])
you = int(input("enter your chooice where\n 1 = stone \n 2 = paper \n 3 =  sicore"))
if((you==1 and computer==3) or (you==2 and computer==1) or (you==3 and computer==3) ):
    print("you win chocie of computer was",computer)
elif (you==computer):
    print("draw")
else :
    print("computer win by choice ",computer)
    
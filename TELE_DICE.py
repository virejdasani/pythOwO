# this is a game inspired by TELEGRAM EMOJIS if you have even used telegram then you know that in that app emojis are animated or moving
# so one day I observed that  DICE emoji when clicked gives different numbers so i decided to play a game with my friend using dice emoji
# and told her that the one who scores the sum up to 100 is the winner and if the person gets a 6 then he/she will get another chance to roll
# and the next day I coded that game in pyhton beacuse i was extremly excited
import random
sum1=0
sum2=0
print("****************WELCOME TO TELEDICE!*****************")
print("For Player 1 enter 1")
print("For Player 2 enter 2")
print("*****************************************************")
# print("Enter 0 to exit/wanna continue enter any character except 0!")
while(1):
    if(sum1>=100):
        print("player 1 wins hurray!")
        break
    elif(sum2>=100):
        print("player 2 wins hurray!")
        break
    input("Player 1:")
    n1=random.randint(1,6)
    print(n1)
    if(n1==6):
            sum1+=6
            n11=random.randint(1,6)
            print("extra chance:")
            print(n11)
            if(n11==6):
                sum1+=n11
                n12=random.randint(1,6)
                print(" second extra chance:")
                print(n12)
                if(n12==6):
                    print("cannot get more chance")
                    sum1+=n12
                    if(sum1==sum2):
                        sum1=sum1-1
                        if(sum1<0):
                             sum1=0
                else:
                    sum1+=n12
                    if(sum1==sum2):
                        sum1=sum1-1
                        if(sum1<0):
                            sum1=0
    else:
        sum1+=n1
        if(sum1==sum2):
            sum1=sum1-1
            if(sum1<0):
                sum1=0
        if(sum1>=100):
            print("player 1 wins hurray!")
            break
    input("Player 2:")
    n2=random.randint(1,6)
    print(n2)
    if(n2==6):
            sum2+=6
            n21=random.randint(1,6)
            print("extra chance:")
            print(n21)
            if(n21==6):
                sum2+=n21
                n22=random.randint(1,6)
                print(" second extra chance:")
                print(n22)
                if(n22==6):
                    print("cannot get more chance")
                    sum2+=n22
                else:
                    sum2+=n22
    else:
        sum2+=n2
        if(sum2==sum1):
            sum2=sum2-1
            if(sum2<0):
                sum2=0
        if(sum2>=100):
            print("player 2 wins hurray!")
            break

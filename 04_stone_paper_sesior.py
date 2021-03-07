import random
computer_decision=random.randint(0,2)
print(computer_decision)
'''
0==stone
1==paper
2==scessior
U-C==W
0-1==1
0-2==0
1-2==2
1-0==1
2-0==0
2-1==2
'''
print("Print 0 for stone, 1 for paper, 2 for scessior")
user_decision=int(input("Enter your choise:- "))


if(user_decision==0 and computer_decision==1):
    print("You choose stone & Computer choose paper")
    print("COMPUTER WINS THE MATCH")
elif(user_decision==0 and computer_decision==2):
    print("You choose stone & Computer choose scessior")
    print("USER WINS THE MATCH")
elif(user_decision==1 and computer_decision==2):
    print("You choose paper & Computer choose scessior")
    print("COMPUTER WINS THE MATCH")
elif(user_decision==1 and computer_decision==0):
    print("You choose paper & Computer choose stone")
    print("USER WINS THE MATCH")
elif(user_decision==2 and computer_decision==0):
    print("You choose scessior & Computer choose stone")
    print("COMPUTER WINS THE MATCH")
elif(user_decision==2 and computer_decision==1):
    print("You choose scessior & Computer choose paper")
    print("USER WINS THE MATCH")
else:
    print("INVALID INPUT")





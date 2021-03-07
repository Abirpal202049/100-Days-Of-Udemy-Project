print("Welcome to the tip calculator")
amount=float(input("What was the total bill? $"))
people=int(input("To how many people do you want to split the bill:-"))
tip=int(input("How much percentage of tip do you want to pay:- "))
tip_amount=((tip/100)*amount)
cal=round(((amount+tip_amount)/people),2)
print(f"Each of you had to pay an amount of :- ${cal}")# Here we are using F-string to concardinate a string and a float
print("Enter Marks Obtained in  6 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())
marksix = int(input())
tot = markOne+markTwo+markThree+markFour+markFive+marksix
avg = tot/6

if avg>=9 and avg<=10:
    print("Your Grade is A1")
elif avg>=8 and avg<9:
    print("Your Grade is A2")
elif avg>=7 and avg<8:
    print("Your Grade is B1")
elif avg>=6 and avg<7:
    print("Your Grade is B2")
elif avg>=5 and avg<6:
    print("Your Grade is C1")
elif avg>=4 and avg<5:
    print("Your Grade is C2")
elif avg>=3 and avg<4:
    print("Your Grade is D")
elif avg>=2 and avg<3:
    print("Your Grade is E1")
elif avg>=0 and avg<2:
    print("Your Grade is E2")
elif avg>=0 and avg<1:
    print("Your Grade is f1")    
else:
    print("you are fail")

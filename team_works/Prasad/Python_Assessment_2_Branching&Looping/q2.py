side_1=int(input("Enter first side "))
side_2=int(input("Enter second side "))
side_3=int(input("Enter third side "))

max_side=max(side_1,side_2,side_3)
print(max_side)

if (side_3==max_side and side_1+side_2>side_3) or (side_2==max_side and side_1+side_3>side_2) or (side_1==max_side and side_1+side_2>side_1):
    print("Triangle possible")
    if (side_1==side_2==side_3):
        print("Equillateral")
    elif(side_1==side_2 or side_2==side_3 or side_1==side_3):
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Triangle not possible")
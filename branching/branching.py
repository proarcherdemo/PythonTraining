x = -10

# Check if the value is +ve

# indentation rules

if x >= 0:  # True
    # this statement will be executed only when the condition is True
    print("Got a +ve number") # Body
else:
    print("-ve number")


if x >= 0:  # False
    # this statement will be executed only when the condition is True
    print("Got a +ve number") # Body

if x < 0: #True
        print("-ve number")


x = 10
# > +ve , < -ve , == 0

if x >= 0:  # True
    # this statement will be executed only when the condition is True
    print("Got a +ve number") # Body
elif x < 0:  # False
    print("-ve number")
elif x == 0:  # False
    print("Zero value")




if x >= 0:  # True
    # this statement will be executed only when the condition is True
    print("Got a +ve number") # Body
elif x < 0:  # False
    print("-ve number")
else:  # Default
    print("Zero value")




# Nested if else
x = 5
print("======")
if x >= 0:  # True
    # this statement will be executed only when the condition is True
    print("Got a +ve number") # Body
    if x > 10 :
        print("Greater than 10")
        if x%2 == 0 :
            print("0")
        else:
            print("non zero")
    else:
        print("Less than 10")

print("Out of IF")






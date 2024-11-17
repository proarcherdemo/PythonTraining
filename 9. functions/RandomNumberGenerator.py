import random

num = random.random()  # random number in the range of 0.0 to 1.0
print(num)

num = random.randint(1, 100)  # random number in integer
print(num)

# Generate a username for login into your banking system
# 1. Generate some username 
# 2. Ensure that it is not duplicated

firstName = "Ramesh"
lastName = "Mehra"

length = len(firstName)

str = firstName[:length-2] + lastName[0] + lastName[-1]
print(str)
rint = (int)(random.random()*9999999)
print(rint)

username = "{}{}".format(str,rint)
print("Username : ", username)


sequenceNo = "From DB"
username = "{}{}{}".format(str,rint,sequenceNo)

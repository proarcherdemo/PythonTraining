# WAP to generate a multiplication table for user provided number.

# O/P
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
#.
#.
# 2 * 10 = 20

'''
num = int(input("Enter the number : "))
terms = int(input("Please enter the number of terms to be printed: "))

i = 1
while i<=terms:
    prod = num * i
    print(num, '*', i, '=', prod)
    i = i + 1



for i in range(1, terms+1):
    prod = num * i
    print(num, '*', i, '=', prod)

'''

# WAP to get number from user and give Factorial
# !5 = 5 * 4 * 3 * 2 * 1
# O/P : 120


num = int(input("Enter the number : "))

fact = 1
while (num >=1):
    fact = fact * num
    num = num - 1

print("Factorial :", fact)


num = int(input("Enter the number : "))
fact = 1
for x in range(1, num+1):
    fact = fact * x

print("Factorial From For :", fact)


fact = 1
for x in range(5, 0, -1):
    fact = fact * x

print("Factorial (For Reverse) :", fact)


# WAP to generate fibonacci series. Take number of terms from user
# 0  1  1  2  3  5  8  13  21  34 .....

# input : n1 = 0,  n2 = 1




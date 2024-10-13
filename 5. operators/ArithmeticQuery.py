# number = 123456
# O/P : 1 + 2 + 3 + 4 + 5 + 6 = 21

# number = 345678
# O/P : 3 + 4 + 5 + 6 + 7 + 8 = 33

num = 345678
sum = 0

remainder = num % 10    # 123456 % 10 = 6
num = num // 10         # 123456//10 = 12345
sum = sum + remainder

remainder = num % 10  # 12345 % 10 = 5
num = num // 10       # 12345 // 10 = 1234
sum = sum + remainder

remainder = num % 10  #1234 % 10 = 4
num = num // 10       #1234 // 10 = 123
sum = sum + remainder

remainder = num % 10  #123 % 10 = 3
num = num // 10       #123 // 10 = 12
sum = sum + remainder

remainder = num % 10  #12 % 10 = 2
num = num // 10       #12 // 10 = 1
sum = sum + remainder

remainder = num % 10  #1 % 10 = 1
num = num // 10       #1 //10 = 0
sum = sum + remainder

print("Sum of digits : ", sum)


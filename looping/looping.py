# use case : print "Hello" 5 times - repeat

#print("Hello")
#print("Hello")
#print("Hello")
#print("Hello")
#print("Hello")

# while loop

count = 0   # initialization

while count < 5:    # 0 < 5=> True, 1 < 5=> True, 2<5=>True, 3<5=>True, 4<5=>True, 5<5=>False
    print("Hello")
    count = count + 1   # 0 + 1 => 1, 1+1 => 2, 2+1=>3, 3+1=>4, 4+1=>5

if count == 5 :
    print("Out of the loop")



# WAP to print numbers from 1 to 10

i = 1

while i<=10:
    print(i)
    i = i + 1


# WAP to print all the even numbers from 1 to 30

i = 1

while i<=30:
    if i%2==0:
        print(i)
    i = i + 1


i = 2
while i<=30:
    print(i)
    i = i + 2


# WAP to print all the numbers that odd and divisible by 5 from 50 till 0 (print the biggest number first)


a=50
while a>=0:   # 0>=0 => True, -1>=0=>False
    if a%2!=0 and a%5==0:
        print(a)

    a=a-1    # 0-1 => -1


# Enhance the previous program to give sum of the numbers.

a = 50
sum = 0

while a>=0:   # 0>=0 => True, -1>=0=>False
    if a%2!=0 and a%5==0:
        sum = sum + a

    a=a-1    # 0-1 => -1

print("Sum : ", sum)




# WAP to return the sum of numbers in below list

#numbers = [1, 2, 3, 4, 5, 6]  # No of elements in list = size of list = 6
numbers = [1, 2, 3, 4, 5, 6, 5, 6, 7, 8]

print(type(numbers))
print("No of elements:", len(numbers))

pos = 0
sum = 0

while pos <= len(numbers)-1:
    sum = sum + numbers[pos]
    pos = pos + 1

print(sum)








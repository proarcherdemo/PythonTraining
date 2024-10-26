
# WAP to generate fibonacci series. Take number of terms from user
# 0  1  1  2  3  5  8  13  21  34 .....

# input1=int(input("enter first value : "))
# input2=int(input("enter second value : "))
# terms=int(input("Enter last limit : "))
# nxtnum=0
# print(input1,input2)
# while(nxtnum<=terms): #"0<3"  "1<3"   "2<3"
#     nxtnum=input1+input2 # "1=0+1"   "2=1+1"  "3=1+2"
#     print(nxtnum)  # "0 1"  "1 2"  "1,3"8
#     input1=input2    # "1"  "1"  "2"
#     input2=nxtnum   # "1"  "2"   "3"

# WAP to generate fibonacci series. Take number of terms from user
# 0  1  1  2  3  5  8  13  21  34 .....

input1=int(input("enter first value : "))
input2=int(input("enter second value : "))
terms=int(input("Enter last limit : "))
sum=0
i=0
print(input1)
print(input2)
while(i < terms-2):
    sum=input1+input2
    print(sum)
    input1=input2
    input2=sum
    i+=1


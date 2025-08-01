num=int(input("Enter number : "))
factors=0

for i in range(1,num+1):
    if(num%i==0):
        factors+=1
if(factors>2):
    print("Not Prime, ", num%10)
else:
    print("Prime, ",num*2)

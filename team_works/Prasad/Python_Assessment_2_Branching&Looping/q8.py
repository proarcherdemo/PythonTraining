n_terms=int(input("Enter the number of terms : "))

num1=0
num2=1

print(num1)
print(num2)
#0 1 1 2 3
for i in range(1,n_terms-1):
    sum=num1+num2
    print(sum)
    num1=num2
    num2=sum    
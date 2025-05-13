num1 = int(input("Enter initial number :"))
num2 = int(input("Enter final number :"))

for i in range(num1,num2+1):
    modulo=i%3
    if modulo%2==0:
        print(i,"%3 ","Even")
    else:
        print(i,"%3 ","Odd")
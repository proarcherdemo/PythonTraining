
num_s=int(input("Enter start number: "))
num_e=int(input("Enter last number: "))

for num in range(num_s,num_e+1):
    factor = 0
    for i in range(1,num+1):
        if num%i==0:
            factor+=1
            #print(factor)
    if(factor==2):
        print(num)


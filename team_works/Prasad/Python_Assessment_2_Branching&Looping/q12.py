year=input("Enter year (YYYY) : ")

if (year[-2:len(year)])=="00":
    if int(year)%400==0:
        print("Leap Year")
    else:
        print("Not a leap year")
elif (year[-2:len(year)])!="00":
    if int(year)%4==0:
        print("Leap year")
    else:
        print("Not a leap year")




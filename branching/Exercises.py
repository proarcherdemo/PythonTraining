# WAP to check whether a number is odd or even

# num = user input

# conditional if else


num = int(input("Enter the number : "))

print(type(num))

if num%2 == 0 :
    print("Even Number")
else:
    print("Odd Number")




# City
# speed limit
# <30 km/hr => Very slow
# >=30 and <50 => Average Speed
# >=50 and <80 => Fast
# >=80 => Fined

# Fine : maxspeed - threshold , 90km/hr - 80 kmhr = 10 km/hr
# rate : Rs. 100 per km/hr violation
# threshold = 80 km/hr

threshold = 80
fine_rate_per_km = 100

speed = float(input("Enter the speed (km/hr) : "))

if speed <30:
    print("You are driving at very low speed.")
elif (speed >= 30 and speed < 50):
    print("You are driving at average speed.")
elif (speed >= 50 and speed < 80):
    print("You are driving very fast.")
else:
    print("You are violating the speed limits.")
    fine = (speed - threshold) * fine_rate_per_km
    print("The fine leived on the violation is Rs.", fine)

# Number data type : Addition, Subtraction, Multiplication, Division (Arithmatic), Comparison,

a = 10  #integer
print(type(a))
print(a)

a = 10.5  #decimal, float
print(type(a))
print(a)

a = 10 + 2j  #decimal, float
print(type(a))
print(a)

# String : concat, replace, trimming
name = "Raj"
print(type(name))
print(name)

# Boolean : True/False : Decision Making
isSunny = True
print(type(isSunny))

taxPaid = False
print(type(taxPaid))

# List : can be modified
x = [10, 20, 30, 40, 50]
print(x)
print(type(x))

x = [10, "Raj", 30.6, 40, "hello"]
print(x)
print(type(x))

# Tuple : can't be modified
x = (10, 20, 30, 40, 50)
print(x)
print(type(x))


# Set : removing duplicates
x = {10, 20, 30, 40, 50, 50, 50}
print(x)
print(type(x))


# Dictionary : key-value

x = {12345678 : "Raj, Pune, Software Engineer"} # key => int, value = String
y = {"ACT0001999" : "Personal, Transaction"} # key => String, value= String

print(x[12345678])
print(y["ACT0001999"])

print(type(x))
print(type(y))





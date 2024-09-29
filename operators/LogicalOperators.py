# and, or, not
# and : Returns true, if all the conditions return true
# or : Returns true, if any o the conditions return true
# not : reverse the output
x = 4

print(x < 10)

print(x == 5)

print(x == 4)


print((x < 10) and (x == 5))  # True and False => False

print((x < 10) and (x == 4)) # True and True => True


print((x > 10) or (x == 4))  # False or True => True

print((x < 10) or (x == 5))  # True or False => True

print((x < 10) or (x == 4))  # True or True => True


print("====NOT=====")
print(not((x < 10) and (x == 5)))




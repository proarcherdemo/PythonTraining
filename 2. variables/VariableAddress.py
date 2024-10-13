# id()
X = 10          #variable_name = value
print(X)
print(type(X))
print("Location of X is ", id(X))
print(type(id(X)))


# addressOf
from ctypes import c_int, addressof
print("Location based on addressof", addressof(c_int(X)))



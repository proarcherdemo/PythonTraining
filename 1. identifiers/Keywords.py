import keyword


kwrds = keyword.kwlist
print("No of keywords = ", len(kwrds))
print(kwrds)

op = "hello" in kwrds  # True/False
print(op)

op = "while" in kwrds  # True/False
print(op)

op = "True" in kwrds  # True/False
print(op)
op = "true" in kwrds  # True/False
print(op)
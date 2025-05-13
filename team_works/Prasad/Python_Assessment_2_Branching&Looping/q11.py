str="PRrasad#@mycompany.com"
print(len(str))
print(str)

if(str[0].isalpha() and str[0:len(str)-14].lower().isalnum()  and str[len(str)-14:len(str)]=="@mycompany.com" and 4<len(str)-14<10):
    print("Valid")
else:
    print("Invalid")


str=input("Enter any sentance to count Vowels and Consonants : ")
i=0

vowels=["a","e","i","o","u"]
vowels_count=0
consonants_count=0
while(i<len(str)):
    if(str[i].lower() in vowels):
        vowels_count+=1
    elif (str[i].isalpha()):
        consonants_count+=1
    i+=1
print("Vowels-",vowels_count)
print("Consonants-",consonants_count)

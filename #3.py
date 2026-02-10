#q3
list1=["Hello", "world", "Python", "java", "Code"]
list_capital=[]

for word in list1:
    if word[0].isupper():
     list_capital.append(word)


print(list_capital)
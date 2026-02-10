#Q5

list1=["HELLO", "World", "PYTHON", "code"]
list_reverse=[]

for word in list1:
    if word.isupper():
        list_reverse.append(word[::-1])
    else:
        list_reverse.append(word)

print(list_reverse)
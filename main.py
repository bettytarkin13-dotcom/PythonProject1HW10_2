#q1

list1=[1,2,3,4,5,6,7]
list_odd=[]
list_even=[]

for i in list1:
    if i%2==0:
        list_even.append(i)
        print('even number',i)
    else:
        list_odd.append(i)
        print('odd number',i)

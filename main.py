# YOUR CODE HERE
lst1=[]
lst2=[]
n=int(input())

for i in range(n):
    lsta = int(input())
    lst1.append(lsta)

for i in range(n):
    lstb = int(input())
    lst2.append(lstb)

def summation(lst1,lst2):
    lst3=[]
    for i in range(len(lst1)):
        add = lst1[i]+lst2[i]
        lst3.append(add)
    return lst3
list_add = summation(lst1,lst2)

def find_min_max (list):
    max=list[0]
    min=list[0]
    for i in list:
        if i > max:
            max=i
    
    for i in list:
        if i < min:
            min=i

    min_max=(min,max)
    return min_max
print(summation(lst1,lst2))
print(find_min_max (list_add))

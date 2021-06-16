#create a list
def createList(r1,r2):
    if(r1==r2):
        return r1
    else:
        res=[]
        while(r1<r2+1):
            res.append(r1)
            r1+=1
        return res

r1=int(input("Enter the starting value of the list"))
r2=int(input("Enter the last value of the list"))
a=createList(r1,r2)
print(a)

#add items to list
c=int(input("Enter the value to be added in the list"))
a.append(c)
print('New List',a)

#delete item from list
a.remove(a[3])
print("List after removing a number is",a)

#to store a largest number in list
def maxnum(a):
    max=a[0]
    for b in a:
        if b > max:
            max=b
    return max
print("The largest number stored in the list is",maxnum(a))

#To store a smallest number in list
def minnum(a):
    min=a[0]
    for d in a:
        if d<min:
            min=d
    return min
print("The smallest number stored in the list is",minnum(a))


#create a tuple
s1=(1,2,3,4,5)
print("Tuple values",s1)

#print the reverse of the created tuple
def reverse(s1):
    new_tup=s1[::-1]
    return new_tup
print("Reverse tuple is",reverse(s1))

#converting the tuple into list
q = (1,2,3)
print("Tuple values is",q)
y = list(q)
print("Tuple converted into list",y)


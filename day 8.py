# Python script to merge two Python dictionaries

def dict(a, b):
    c=a.copy()
    c.update(b)
    return c
    
x = {'oraNGE': 1 , "white" : 2 , "blue"  : 3 }
y = {"Pink" : 4 , "green" : 5 , "lavender" : 6 }  
z = dict(x,y)
print("The Merged dictionaries are ",z)

#program to sort the value from descending to ascending in list and convert it in to a set.
A=[1,3,5,7,15,9,8,13,16]
A.sort(reverse=True)
print("The Value in descending order is ",A )
A.sort()
print("The Value in Ascending order is ",A )

S_1 = set(A)
print("The set value is ",S_1)

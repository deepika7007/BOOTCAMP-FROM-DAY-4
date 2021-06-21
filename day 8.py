# Python script to merge two Python dictionaries

def dict(a, b):
    c=a.copy()
    c.update(b)
    return c
    
x = {'oraNGE': 1 , "white" : 2 , "blue"  : 3 }
y = {"Pink" : 4 , "green" : 5 , "lavender" : 6 }  
z = dict(x,y)
print("The Merged dictionaries are ",z)

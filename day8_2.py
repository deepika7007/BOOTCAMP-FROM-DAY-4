#Write a Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function.
dictionary = {"Kiran":[3, 6, 7],
              "Ammu"  :[5, 12, 16],
              "Sweety":[32,36,35]}
print("The original dictionary is : "+ str(dictionary))
r = dict()
for key in sorted(dictionary):
        r[key] = sorted(dictionary[key])
print("The sorted dictionary : " +str(r))

#Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.

def change_char(str1):
    char = str1[3]
    str1 = str1.replace(char, '$')
    str1 = char + str1[1:]
    
    return str1
print(change_char("orange"))

#Write a Python program to get a string from a given string where all occurrence of its frist char have been changed to capital letter

def function():
    user=input("Enter the string : ")
    return user.capitalize()

function()

#Write a Python program to find the repeated items of a list

a =[3,5,6,7,3,7,6,5,3,7,7]
print(a)
b = a.count(7)
print(b)

#Write a Python program to check the sum of three element and divided by a value which is given as an input by the user

X=int(input("Enter a value : "))
Y=int(input("Enter a value : "))
Z=int(input("Enter a value : "))
sum = X+Y+Z
print(sum)
div=int(input("Enter a number to divide the  sum "))
if (sum% div)==0:
    print("The input value divide the sum ")
else :
    print("The  input value does not divide the sum ")

#Write a Python program to find the Mean,median,mode among three given numbers

x = input("Enter the first number ")
y = input("Enter the second number ")
z = input("Enter the third number ")
print("the Median of the above three numbers")
if y < x and x < z:
    print(x)
elif z < x and x < y:
    print(x)
elif z < y and y < x:
    print(y)
elif x < y and y < z:
    print(y)
elif y < z and z < x:
    print(z)
elif x < z and z < y:
    print(z)

#Write a Python program to swap cases of a given string

a="Deepika"
b="Rajan"
r=a
a=b
b=r
print(a,b)

dec = 367

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

import random as r
import string as st

#In this code, we are going to see about how random passwords can be created using python library function
#"random" and "string".

#Inorder to run this code you must have python3 module and must have installed random and string library functions.

a=list(st.ascii_lowercase)

b=list(st.ascii_uppercase)

c=['!','@','#','$','%','^','&','*']

d=['0','1','2','3','4','5','6','7','8','9']

pw=a+b+c+d

print("Enter the length of the password:")

l=int(input())

password="".join(r.sample(pw,l))

print("Your password:")
print(password)
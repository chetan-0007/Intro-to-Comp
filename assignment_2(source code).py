#Question1
print("Question 1")

string="Python is a case sensitive language"

# a
print("a)",len(string))

#b
print("b)",string[::-1])

#c
new_string=string[slice(10,26)]
print("c)",new_string)

#d
print("d)",string.replace("a case sensitive", "object oriented"))

#e
print ("e)", string.index('a'))

#f
print("f)", string.replace(" ",""))



#question 2
print("\n\nQuestion 2")

name="Chetan"
SID="21103059"
department_name="CSE"
CGPA=str(9.9)


text ="Hey abc here! \nMy SID is XXXX \nI am from xyz department and my CGPA is XX"

text=text.replace("abc",name)
text=text.replace("XXXX",SID)
text=text.replace("xyz",department_name)
text=text.replace("XX",CGPA)

print(text)



#question 3

print("\n\nQuestion 3")

a=56
b=10
print("For a=56 and b=10")

print("a) a&b = ",a&b)

print("b) a|b = ",a|b)

print("c) a^b = ",a^b)

print("d) a<<2 = ",a<<2)
print("   b<<2 = ",b<<2)

print("e) a>>2 = ",a>>2)
print("   b>>4 = ",b>>4)



#Question 4
print("\n\nQuestion 4")

#enerting of numbers by user
num1=int(input("Enter first number:\n"))
num2=int(input("Enter second number:\n"))
num3=int(input("Enter third number:\n"))

if num1>num2:
    num=num1  #num is the number greatest between num1 and num2
else:
    num=num2

if num>num3:
    greatest=num
else:
    greatest=num3

print("The greatest number is: ", greatest)



#question 5
print("\n\nQuestion 5")
print("To check if 'name' is present in string enetered by user")

string=input("Enter any text:\n")

if "name" in string:
    print("YES")
else:
    print("NO")



#question 6

print("\n\nQuestion 6")
print("To check if it is poosible to form triangle by lenth of three sides given by user")

len1=int(input("Enter length of first side (in cm):\n"))
len2=int(input("Enter length of second side (in cm):\n"))
len3=int(input("Enter length of third side (in cm):\n"))

if len1>=len2+len3:
    print("NO")
elif len2>=len3+len1:
    print("NO")
elif len3>=len1+len2:
    print("NO")
else:
    print("YES")

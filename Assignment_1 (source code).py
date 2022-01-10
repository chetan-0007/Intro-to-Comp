#Question 1
# finding average of three numbers entered by user

print ("Question 1")

number_1=input("enter 1st number: ")
number_2=input("enter 2nd number: ")
number_3=input("enter 3rd number: ")

number_1=int(number_1)
number_2=int(number_2)
number_3=int(number_3)

average=(number_1+number_2+number_3)/3
print("the average of three numbers are :", average)


#Question 2
#computing person's income tax

print ("\n\nQuestion 2")

Gross_income=int(input("Enter your gross income: $"))
Standard_deduction=10000 #(in $)
n=int(input("enter number of dependents :")) #n=number of dependents
dependent_deduction=n*3000

taxable_income=Gross_income - Standard_deduction - (n*dependent_deduction)

Tax= taxable_income*20/100

print("TAX: $", Tax)



#   Question 3
#Storing diff datatype in list
print("\n\nQuestion 3")

#entering required fiels
SID=int(input("Enter your SID:\n"))
Name=input("Enter your name:\n")
Gender=input("Enter M for male or\n      F for female or\n      U for unknown\n")
Course_Name=input("Enter your course name:\n")
CGPA=int(input("Enter your CGPA:\n"))

Student=[SID, Name, Gender, Course_Name, CGPA]

print("Student",Student)




#question 4
#Displaying marks of students in list and sort them
print("\n\nQuestion 4")

#Marks of 
Student1=int(input("Enter marks of 1st student:\n"))
Student2=int(input("Enter marks of 2nd student:\n"))
Student3=int(input("Enter marks of 3rd student:\n"))
Student4=int(input("Enter marks of 4th student:\n"))
Student5=int(input("Enter marks of 5th student:\n"))

#making list of marks
Marks=[Student1, Student2, Student3, Student4, Student5]

#sorting makrs
Marks.sort()

print(Marks)




#Question 5
print("\n\nQuestion5")
Color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(Color)

#part a 
print("\nQuestion 5 (part a)")
Color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#Removing 4th element from the list
Color.remove(Color[3])
print(Color)

#part b
print("\nQuestion 5 (part b)")
Color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#removing 'black' and 'pink' from list and replacing it with 'purple'
Color.remove('Pink'), Color.remove('Black'), Color.insert(3,'purple')
print(Color)

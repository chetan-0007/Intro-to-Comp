#QUESTION 1

print("Solution 1\n")

#crearting a function
def Tower_of_hanoi(n,source,target,auxiliary):
    if n==1:
        print(f"move disc 1 from rod {source} to {target}")
        return
    Tower_of_hanoi(n-1,source,auxiliary,target)   #function calling itself (recursion)
    print(f"move disc {n} from rod {source} to {target}")
    Tower_of_hanoi(n-1, auxiliary, target, source)


n=3  #n=number of discs
print(f"Steps to be followed for {n} number of discs are as followed:\n")
#calling function
Tower_of_hanoi(n,'A','B','C')   #where n=no of discs, A=souce, B=target, C=auxiliary




#QUESTION 2

print("\nSolution 2\n")

#input rows from user
n = int(input("Enter the number of rows in Pascal's Triangle: "))

#using recursions
print("\nprinting triangle using recursions:\n")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    print('  '*(originaln-n), end='')

    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#alt method

#using loops
print("\nprint pascal triangle using loops:\n")
for line in range(1, n+1):

    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()









#QUESTTION 3

print("\nSolution 3")
#Taking input from the user
n1=int(input("\nEnter an Integer:\n"))
n2=int(input("Enter another Integer:\n"))

#Making a list of return values
list1=list(divmod(n1,n2))

quotient=list1[0]
remainder=list1[1]


print(f"\nThe quotient when {n1} is divided by {n2} is {quotient}.")
print(f"The remainder when {n1} is divided by {n2} is {remainder}.")

#.a
print("\na)")
z=callable(divmod(n1,n2))
if z==True:
    print(f"Function is callable")
if z==False:
    print(f"Function is non-callable")


#.b
print("\nb)")
#list of values
list1=[quotient,remainder]
zero=False

if zero in list1:
    zero=True
else:
    zero=False

if zero==True:
    print("All values are NOT 'non-zero'")
elif zero==False:
    print("All values are 'non-zero'")


#,c
print("\nc)")
#new values of list
list2=[quotient,remainder]
for i in range (4,7):
    list2.append(i)
print(f"Appended (4,5,6) in the values ({quotient},{remainder})")
listv2=[]

for i in list2:
    if i>4:
        listv2.append(i)

listv3=list(map(str,listv2))

v=",".join(listv3)
print(f"Values greater than 4 is {v}")


#.d
print("\nd)")
set1={1,2}
set1.clear()
#adding above result in set datatype
for el in listv2:
    set1.add(el)
print("Above result in set form is shown below:")
print(set1)


#e
print("\ne)")
#Making set1 immutable
frozenset(set1)
print("The above set has been converted to immutable.")


#f
print("\nf)")
print(f"Max value from set is {max(set1)}")
#using hash function
hash_value=hash(max(set1))
print(f"Hash value of {max(set1)} is {hash_value}")














#QUESTION 4

print("\n\nSolution 4\n")

#creating a class
class Student:

    def __init__(self,name,roll_no):   #using constructor
        print("An object is created")
        self.name=name
        self.roll_no=roll_no

    def get_details(self):
        print(f'\nName: {self.name} \nRoll no: {self.roll_no}')
        
    def __del__(self):
        print(f"\nThe object with student name {self.name} is deleted")


#creating objects

Student_1=Student('Chetan', 211)
Student_2=Student('ABC', 221)
Student_1.get_details()
Student_2.get_details()











#  QUESTION 5

print("\nSolution 5\n")
 
#creating a class
class Employee:
    
    def __init__(self, name, salary):   #constructor to create objects
        print("\nAn emplyee is created")
        self.name=name
        self.salary=salary

    def get_details(self):
        print(f"Name: {self.name} \nSalary: {self.salary}")


#creating objects

employee_1=Employee('Mehak', 40000)
employee_1.get_details()

employee_2=Employee('Ashok', 50000)
employee_2.get_details()

employee_3=Employee('Viren', 60000)
employee_3.get_details()
del employee_3   #deleting object
print("Employee 3: Viren is deleted")







print("\nSOLUTION 6")

print("\nFRIENDSHIP CHALLANGE")
#definig anagram
def anagram(word1,word2):
    
    #converting letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    
    #form empty list to store letters of words
    l1=[]
    l2=[]
    for e in word1:
        l1.append(e)
    for el in word2:
        l2.append(el)
   
    #sorting the list
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

#taking player name input
player1=str(input("\nEnter Player1 name:"))
player2=str(input("Enter Player2 name:"))

#taking words by each player
word_of_player1=str(input(f"\nEnter Word by {player1}:"))
word_of_player2=str(input(f"Enter Word by {player2}:"))

#using anagram function
result=anagram(word_of_player1,word_of_player2)

if result==True:
    print(f"\nCongratulations: Friendship of {player1} and {player2} is Real")
elif result==False:
    print(f"\nSorry: Friendship of {player1} and {player2} is Fake")
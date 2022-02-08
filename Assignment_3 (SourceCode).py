#QUESTION 1
print("SOLUTION 1\n")

string=input("Enter text:\n")    #taking string as input from user 
string=string.lower()   #making all text in string to lower case
c=len(string)  #c=number of letters in string

#dividing string into a list with each word as its element
a=string.split()

b=len(a)  #b=number of items in list


#if string contains only 1 word, then counting occurance of each letter
if b==1:
    dict={}  
    for x in range(0,c):
        dict.update({string[x]:string.count(string[x])})
    print("\nReqired dictionary with each letter of word as key and its's repitation as value:\n",dict)    
    
#if string contains more than 1 word, then counting occurance of each word
elif b>=1:
    dict={}
    for i in range(0,b):
        dict.update({a[i]:a.count(a[i])})
    print("\nReqired dictionary with each word of string as key and its's repitation as value:\n",dict)   

else :
    print("\nPlease enter any text")










#QUESTION 2
print("\nSOLUTION 2\n")


year =int(input("Enter year: "))  #taking year as input from user

#checking if entered year is a leap year
if year%4==0:
    leapyear=True
else:
    leapyear=False


if year in range(1800,2026):
    Month=int(input("Enter month: ")) #taking month as input from user
    
    if Month in (4,6,9,11):      #for months having 30 days
        day=int(input("Enter day: "))
        if day in range(1,30):
            print(f"Next date in the format(dd/mm/yyyy) is: {day+1}/{Month}/{year} ")
            
        elif day==30:
            print(f"Next date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{year} ")
            
        else:
            print("Error: enter corrent day (1-30 for this month)")
    
    elif Month in (1,3,5,7,8,10):  #for month having 31 days
        day=int(input("Enter day: "))
        if day in range(1,31):
            print(f"Next date in the format(dd/mm/yyyy) is: {day+1}/{Month}/{year} ")
        elif day==31:
            print(f"Next date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{year} ")
            
        else:
            print("Error: enter corrent day (1-31 for this month)")

    elif Month==12:  #for december
        day=int(input("Enter day: "))
        if day in range(1,31):
            print(f"Next date in the format(dd/mm/yyyy) is: {day+1}/{Month}/{year} ")
            
        elif day==31:
            print(f"Next date in the format(dd/mm/yyyy) is: {1}/{1}/{year+1} ")
            
        else:
            print("Error: enter corrent day (1-31 for this month)")

   
    elif Month==2:  #for february
        if leapyear==True:   #if entered year is leapyear
            day=int(input("Enter day: "))
            if day in range(1,29):
                print(f"Next date in the format(dd/mm/yyyy) is: {day+1}/{Month}/{year} ")
                
            elif day==29:
                print(f"Next date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{year} ")
                
            else:
                print("Error: enter corrent day (1-29 for this month)")

        elif leapyear==False:  #if entered year is non leap year
            day=int(input("Enter day: "))
            if day in range(1,28):
                print(f"Next date in the format(dd/mm/yyyy) is: {day+1}/{Month}/{year} ")
                
            elif day==28:
                print(f"Next date in the format(dd/mm/yyyy) is: {1}/{Month+1}/{year} ")
                
            else:
                print("Error: enter corrent day (1-28 for this month)")
            
    else:
        print("Error: enter correct month (1-12) ")

else:
    print("Error: enter year in range (1800-2025)")











#Question 3

print("\nSOLUTION 3\n")

n=int(input("How many terms to be entered in list?:\n"))    #taking no. of terms to be in list as input from user

list=[] 
for i in range(1,n+1):
     element=int(input(f'Enter required element:\n'))  #taking elements of list as input from user
     list.append(element)

#making empty list and store the elemments enerted by user along with its square
Req_list=[]   
i=0
for i in range (0,n):  
     Req_list.append((list[i], list[i]**2))
     i=i+1

print("\nThe required list is:\n",Req_list)










#Question 4
print("\nSOLUTION 4\n")

grade_points=int(input("Enter your grade point: "))  #taking grade points as input from user


if 4<=grade_points<=10:
    if grade_points==10:
        grade="A+"
        performance="Outstanding"

    elif grade_points==9:
        grade="A"
        performance="Excellent"

    elif grade_points==8:
        grade="B+"
        performance="Very Good"

    elif grade_points==7:
        grade="B"
        performance="Good"

    elif grade_points==6:
        grade="C+"
        performance="Average"

    elif grade_points==5:
        grade="C"
        performance="Below Average"

    elif grade_points==4:
        grade="D"
        performance="Poor"

    print(f"Your grade is '{grade}' and {performance} performance")

else:
    print("Error (Grade points should be in range 4-10")










#Question 5

print("\nSOLUTION 5\n")

string='ABCDEFGHIJK'   

for i in range(0,6):
    print(' '*i,string[0:(11-(i*2))])   #entering an extra scape and removing last two letters from string wuth each loop










#Question 6
print("\nSOLUTION 6")


dict={}        #making an empty list in which name and sid to be stored
i="y"          #Making 1st entry as default
if i=="y" :
    while i=="y" or i=="Y":              #continouly asking name and sid and storing it in empty dictionary till user enters y
        a=str(input("\nEnter name: "))   #taking name as input
        b=int(input("Enter SID: "))      #taking SID as input
        if b<=0:
            print("ERROR: SID should be positive integer")
            exit()
        dict.update({a:b})               #storing name and sid in dictionary (name as key, SID as value)
        print(dict)
        i=input("\nWant to make another entry?\n Press 'Y' for YES / 'N' for NO.\n")    
                                         #asking user if want to a make another entry
        
        
    if i=="n" or i=="N":                 #if user enters 'N', code progresses
        
        #part a)
        print("\na) The required dictionary is\n",dict)  
        
       
       
        #part b)
        list_1=dict.keys()               #making a list(list_1) containg (dictionary's keys) names
        sorted_list_1=sorted(list_1)     #sorting list on the basis of names
       
        new_dic_1={}                     #making a new dictionary sorted on  the basis of name
        for items in sorted_list_1:
            new_dic_1.update({items:dict.get(items)})

        print("\nb) Dictionary sorted on the basis of names:\n",new_dic_1)
        

        
        # part c)
        rev_dict={}                     #making a new dict with SIDs as keys and name as values
        for key,value in dict.items():
            rev_dict.update({value:key})

        list_2=rev_dict.keys()          #making another list(list_2) containg SIDs
        sorted_list_2=sorted(list_2)    #sorting list on the basis of SIDS
        
        
        new_dic_2={}                    #making a new dictionary sorted on  the basis of SIDs
        for items in sorted_list_2:
            new_dic_2.update({rev_dict.get(items):items})

        print("\nc) Dictionary sorted on the basis of SID:\n",new_dic_2)

        

        #part d)
        SID=int(input("\nd) Enter a SID to get it's name:"))  #Taking SID as input to print the name assigned with it
        if SID in list_2:
            print("Name related to following sid is: \n",rev_dict.get(SID))
        else:
            print("ERROR: The following SID is not present in dictionary")

   
   
   
    else:
        print("ERROR: Enter 'Y' or 'N' only" )












# Question 7
print("\nSOLUTION 7\n")


n=int(input("How many terms to be printed in fibonacci series?\n"))  #taking n as input from user for how many terms of Fibonacci sequence to be printed

n1=0   
n2=1

if n<=0:
    print("ERROR: enter a postive number")

else:
    list=[]   #making an empty list
    for i in range (0,n-1):
        if i==0:
            list.append(n1)    #entering '0' as first term in list
        if i==1:
            list.append(n2)    #entering '1' as second term in list
            continue
        sum=n1+n2
        n1=n2
        n2=sum
        list.append(sum)      #entering the remaing terms
        sum+=sum

    print("\nRequired Fibonacci series is:\n",list)

    
    #calculating sum of all terms present in list
    sum=0
    for items in list:
        sum=sum+items
    #calculating average
    average=sum/len(list)  #len(list)=no. of elements in list
    print("\nAverage of following series is:\n",average)











    #QUESION 8
print("\nSOLUTION 8\n")

set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

#part a
print("a)",end=" ")
a=(set1^set2)  #a=(set1|set2)- (set1&set2)
print(a)


#part b
print("b)",end=" ")
b=(set1^set2^set3)  # b=(set1|set2|set3)- (set1&set2)- (set2&set3)- (set3&set1)
print(b)

# part c
print("c)",end=" ")
print((set1|set2|set3)-(set1^set2^set3)-(set1&set2&set3))  
    #(union of all sets)- (elements present in only one set) - (elements present in all three sets)

#part d
print("d)",end=" ")
integers={1,2,3,4,5,6,7,8,9,10}
print(integers-set1)

#part e
print("e)",end=" ")
print(integers-(set1|set2|set3))   #( integers) - (union of set1,set2 and set3)
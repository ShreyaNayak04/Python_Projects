# 13/11/2021

# shreya
# lalalallll
# eeee
# print("shreya nayak")# to print anything u want


# playsound
''' 
from playsound import playsound
playsound(path) # different modules can be downloaded by using pip install module name
'''


# os module
'''
import os
print(os.listdir()) # used to list the files that are created in this folder
'''


#variables and datatypes
'''
a='shreya'  #string
b = 5       #integer
c = 12.5     #float
d=True      #boolean
e=None      #none

print(a)#printing the variables
print(b)
print(c)
print(d)
print(e)

#printing the type of variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
'''


# arithmetic operators
'''
a=2
b=5
print("The value of a+b",'=',a+b)
print("The value of a-b",'=',a-b)
print("The value of a*b",'=',a*b)
print("The value of a/b",'=',a/b)
print("The value of a%b",'=',a%b)
'''

# Assignment operators
'''
a=5
b=5
c=2
d=3
b-=2
a+=2
c*=2
d/=2
print(a)
print(b)
print(c)
print(d)'''


# comparison operators
'''
a=(12>4)
print(a)
b=(2<4)
print(b)
c=(2>=5)
print(c)
'''


# Logical operators
'''
bool1=True
bool2=False
print("The value of bool1 and bool2 is",(bool1 and bool2))
print("The value of bool1 and bool2 is",(bool1 or bool2))
print("The value of  bool2 is",( not bool2))
'''

# 14/11/2021

# typecasting

# integer
'''
a="125"
a=int(a)
print(a + 5)

# string
b="shreya"
b=str(b)
print(b + " nayak")
'''
# input function
'''
a=input("Enter your name")
print(a)
'''

# add two numbers
'''
a=(input("enter a number:"))
b=(input("enter a number:"))
sum=float(a)+float(b)
print('sum of {0} and {1} is {2}'.format(a,b,sum))
'''

# program to get remainder

# by taking user input
'''
print("The remainder when a is divided by b is",a%b)
a=input("Enter a number:")
b=input("Enter a number:")
remainder=float(a)%float(b)
print("The remainder of {0} and {1} is {2}".format(a,b,remainder))
'''


# average of two numbers
'''
a=input("Enter first number:")
b=input("Enter second number:")
a=int(a)
b=int(b)
avg=(a+b)/2
print("Average of a and b is",avg)
'''


# strings
'''
a="shreya"
print(type(a))
b="shreya's"
print(b)
'''
# triple quotes is used when we want to create a paragraph

# string slicing
'''
a="Good morning,"
b=" shreya"
print(a+b)
'''

# index in strings

'''
a="shreya"
print(a[1])
print(a[0:4])
'''
# if we want to start the index from the right to left side then it starts from -1
'''
a="shreya"
print(a[3:-1])
'''
# 15/11/2021
# string functions
'''
quotes=("peace is always beautiful")
print(len(quotes))
print(quotes.endswith("beautiful"))
print(quotes.endswith("shreya"))
print(quotes.count('e'))
print(quotes.count('peace'))
print(quotes.capitalize())
print(quotes.find("Peace"))
print(quotes.find("beautiful")) #returns the index of the first occurence
print(quotes.replace("peace", "trust"))
'''
# exercise
'''
a=input("Enter your name")
print(a)
b=("Good afternoon"+a)
print(b)
'''


# 16/11/2021
# program to detect the double spaces

# double space is present
'''
st="My name is shreya  nayak"
doublespaces=st.find("  ")
print(doublespaces)
'''

# double space is not present
'''
st="My name is shreya nayak"
doublespaces=st.find("  ")
print(doublespaces)
'''
'''
st="My name is shreya nayak"
singlespaces=st.find(" ")
print(singlespaces)
'''


# list
# values can be repeated 
'''
a=[1,2,3,4,5]
a[2]=25
print(a)
print(a[2])
print(a[5])
a=[1,"shreya",12.5,True]
print(a)
'''

# list slicing

'''
fav=["Damon","Stefan","Jeremy","Klaus","Alena"]
print(fav[0:4:3])
'''

# wrong syntax
'''
list1=[4,3,1,8,9]
 list2=list1.sort() 
 print(list2)
'''
#  correct syntax

'''
list1=[4,3,1,8,9]
list1.sort()
print(list1) 
list1.reverse()
print(list1)
list1.append(10)
print(list1)
list1.insert(2, 20)
print(list1)
list1.pop(4)            # a number will be removed by considering the index
print(list1)
list1.remove(10)
print(list1)            # it will directly remove the element from the list

'''

# Tuples
'''
s = (1, 2, 3, 4, 5)
print(s)
print(s[1])
#s[2] = 6            # we cannot change the existing value
s1 = (1,)           #tuple with one element is declared in this way
print(s1)
s = (1, 2, 3, 4, 5)
print(s.count(1))
print(s.index(5))    # it wiil return the starting index of number 1
'''


# practice 
# program to print the name of the fruits by taking user input
'''
f1=input("Enter The Fruit Number 1")
f2=input("Enter The Fruit Number 2")
f3=input("Enter The Fruit Number 3")
f4=input("Enter The Fruit Number 4")
f5=input("Enter The Fruit Number 5")
f6=input("Enter The Fruit Number 6")
f7=input("Enter The Fruit Number 7")
fruitList=[f1,f2,f3,f4,f5,f6,f7]
print(fruitList)
'''


# dictionaries
# key,values
'''
mydict={
    "Name":"shreya",
    "Age":18,
    "anotherdict":{"blahhh":"laaa"},
    "marks":[1,2,3]                    # list values can also be used
}
print(mydict)
print(mydict["Name"])
print(mydict["anotherdict"])
print(mydict["anotherdict"]["blahhh"])
print(mydict["marks"])
mydict["Age"]=20    #value can aslo be changed
print(mydict)
print(type(mydict.keys()))   #it will give the type of keys
print(list(mydict.keys()))    #can be converted to list
print(type(mydict.values()))  #used to print the values
print(mydict.values()) 
print(mydict.items())       #it will print the whole tuple
print(mydict)             
mydict1={
    "fav":"damon"
}
mydict.update(mydict1)        #used to add a new element
print(mydict)
print(mydict.get("fav"))   #used to access the particulat element and it won't throw a error
'''




# 17/11/2021
'''
# sets 
# set is a collection of non repeated values
a=set()  #it will create an empty set
print(a)

b=set()
print(type(b)) #type will be set in this case


# element can be inserted into the set
'''


'''
c=set()
c.add(5)
c.add(4)
c.add((1,2,3))  #example of adding a tuple into the set
print(c)
print(len(c))             #gives the length of the set
c.remove(4)                #it removes the element
print(c)              
#c.remove(15)             #throws an error
c.pop()
c.clear()


print(c)
'''
# list and dictionary cannot be added into the set but tuple can be added into the set

# it is not poosible to access the elements of the set


'''
# practice
mydict={
    "billi":"cat",
    "kuttha":"dog",
    "tum":"you"
}
print("The options are:",mydict.keys())
a=input("Enter the hindi word:")
print("The meaning of the hindi word is:",mydict[a])
'''

'''
s={18,"18"}
print(s)
'''


'''
s=set()
s.add(20)
s.add("20")
s.add(20.5)
s.add(20.0)             # 20 and 20.0 is same 
print(len(s))
'''


'''
s={}
print(type(s))    # it wiil print dict because of {}
'''

# conditional expression
# if and else
'''
a=5
if(a>10):
    print("a is greater than 20")
else:
    print("a is less than 20")   
'''


# else if
'''
a=12
if (a>20):
    print("a is greater than 20")
elif (a==0):
    print("a i sequal to  0")
else:
    print("a is less than 20") 
'''


# program by taking the user input
'''
age=int(input("Enter your age:"))
if(age>18):
    print("YES")
else:
    print("NO")  
''' 


     
'''
 relational operators
 ==,>=,<=
'''



'''
logical operators
if(age>12)and(age<15):
if(age>12)or(age<15):
not
'''



'''
a=[1,2,3,4]
print(5 in a)
'''

# 18/11/2021
# program to print whether the given text is spam or not
'''
text=input("Enter the text")

if("lot of money " in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("click this" in text):
    spam=True
else:
    spam=False        
if(spam):
    print("This text is spam")
else:
    print("This text is not spam")    
'''


# 19/11/2021
# loops

'''
# while loop
i=5
while(i<10):
    print("YES")
    print(" YES ",str(i))
    i=i+1
# it will stop executing this line when the condition becomes false
'''


'''
i=0
while(i<5):
    print("shreya nayak")
    i=i+1
'''

# output is not correct
'''
friends=['sushanth','shadow','shravya','raksha','shridhar'] 
i=0
while (i<len(friends)):
    print(friends[i])  
i=i+1
'''



'''
# for loop
s=[1,2,3,4]
for item in s:
    print(item)
'''



'''
for i in range(10):
    print(i) 
      
for i in range(2,10):
    print(i) 
'''



# use of else 
'''
s=[1,2,3,4]
for item in s:
    print(item)
else:
    print("done")
'''
    
#  use of break   
'''
for i in range(10):
    print(i)
    if i==5:
        break
'''       

# use of continue
'''
for i in range(10):
   
    if i==5:
        continue
    print(i)

'''


# pass statement
# pass is used to do nothing it is just a null statement
'''
s=[1,2,3,4]
for item in s:
    pass
'''

# program to create a multiplication table
'''
num=int(input("Enter a number:"))
for i in range(1,11):
    print(str(num) + " X " + str(i) + " = " + str(i*num))

'''


# greet the people whose name starts with S 
'''
s1=["Shreya","Damon","Stefan"]
for name in s1:
    if name.startswith("S"):
        print("Hello " + name )
    
'''


# program to print whether the given number is prime or not 
'''
num=int(input("Enter a number:"))
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        
if prime:
    print("Given number is prime")
else:
    print("Given number is not prime")        

'''

# 22/11/2021

# program to print a factorial of a given number
'''
num=int(input("enter a number :"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
#print(f"The factorial of this number is {factorial}") 
print(f"The factorial of {num} is {factorial}") 
'''


'''
n=4
for i in range(4):
    print("*" * i)
'''

#8/12/2021

# function
'''
def greet(name):
    print("Good day "+ name)
greet("Shreya")  
'''
  
'''
def greet(name):
    sh="good morning " +name
    return sh
a=greet("shreya")
print(a)
'''

# 9/12/2021
# default argument
'''
def greet(name=  "stranger :) "):
  print("good day " +name)
greet("shreya")
greet()
'''

# recurion function="the function which calls itself is called as recursive function"
'''
def factorial(n):
    if(n==0) or (n==1):
        return 1
    else:
       return n*factorial(n-1)
num = 5
print ("Factorial of",num,"is",
      factorial(num))
'''


'''
def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
m=maximum(2,4,5)
print("The value of maximum is "+str(m))           
  '''
# print("Flush,\nthe toxic peoples,\ninto the toilet :)...\n")


# program to print the star
'''
n=5
for i in range(n):
    print(" * " * (n-i))
'''


# it removes the space
'''
this="            Shreya is a bad girl             "
print(this)
print(this.strip())
'''




# 10/12/2021
# used to read the content of file
'''
f=open('sample.txt','r')
data=f.read()     #it will read all the contents of a file
data=f.read(2)    #it will read only 2 characters of a file
data=f.readline() #it will read a line from a file
print(data)
f.close()
'''



'''
f=open('sample.txt','r')
t=f.read()
if 'shreya' in t:
    print("Shreya is present")
else:
    print("Shreya is not present")
        
f.close()
'''


'''
for i in range(1,21):
    with open(f"tables\multiplication_table{i}",'w') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")
    break
 
'''

# replaces donkey with #####
'''
with open('another.txt') as f:
    content=f.read()
    content=content.replace('donkey', '#######')
with open('another.txt','w') as f:   
    f.write(content)
'''

# object oriented programming
# class contains variables or methods
# class is a blueprint of a object

'''
All the revisions are done...
Now some coding practice is needed...
Lets create some own programs
'''


# a='''my name
# is
# shreya
# nayak'''
# print(a)

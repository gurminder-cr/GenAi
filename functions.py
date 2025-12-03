# functions - 
# pre-defined functions - print, input() 
# user-defined functions 
# def keyword is used to create function


# simple function
# def printSomething():
#     print("Hello Class")
#     print('hi')
# printSomething()

# function with return 
def funcRet():
    # print('Hello Anurag')
    return "Ansh"
    print(1234)
# a=funcRet()
# print(a)
# print(funcRet())

# function with parameter or argument
# def argsfunc(a,b): # parameters
#     return a+b 

# i=int(input('enter i '))
# j=int(input('enter j '))
# ans=argsfunc(i,j)  # arguments 
# print(ans)


# keyword arguments 

# def keyArgs(a,b,c):
#     print(a,b,c)

# # i=10  
# # j=20
# # k=30
# # keyArgs(a=10,b=20,c=30)
# keyArgs(c=10,b=20,a=30)



# default argument 

# def sumss(a=4,b=10):
#     print(a+b)
def sumss(a,b=10):
    print(a+b)
    
# sumss()
# sumss(3,5)



# Given a dictionary employee_details where the keys are employee IDs and values are dictionaries with name, department, and salary, filter and create a list of names of employees who have a salary greater than 50,000.

employee_details={
    '1':{
        'name':'Ansh',
        'department':'HR',
        'salary':60000
    },
    '2':{
        'name':'Anurag',
        'department':'IT',
        'salary':45000
    },
    '3':{
        'name':'Shubam',
        'department':'Dm',
        'salary':55000
    }
}
l=[]
for i,j in employee_details.items():
    print(i,j)
    if j['salary']>50000:
        l.append(j['name'])
        
print(l)


# Write a program to count the number of vowels in a given string
naam='Gurminder Singh'
vow='aeiouAEIOU'
count=0
v=[]
for i in naam:
    if i in vow:
        count+=1
        v.append(i)
print(count)
print(v)
print(len(v))
# for loop in function
# def loopFunc(a):
#     # print(a)
#     sum=0
#     for i in a:
#         sum+=i
    
#     return sum 

# # loopFunc([34,66,55,12,11])
# print(loopFunc([34,66,55,12,11]))

# Arbitrary Arguments -  *args 

# def sumsAll(*a):
#     sum=0
#     for i in a:
#         sum+=i
#     return sum

# print(sumsAll(12,14))
# print(sumsAll(12,14,33))
# print(sumsAll(12,14,33,55))
# print(sumsAll(12,14,33,55,44))



# keyword arbitrary arguments - **kwargs
def keywordArgs(**a):
    sum=0
    for i in a.values():
        sum+=i
    return sum
    
# print(keywordArgs(a=10,b=20))
# print(keywordArgs(a=10,b=20,c=30))
# print(keywordArgs(a=10,b=20,c=30,d=40))
# print(keywordArgs(a=10,b=20,c=30,d=40,e=50))


# lambda function - one line/single line function/ anonymous functions 

# variable-name= lambda parameters: print()
# variable-name= lambda parameters: a+b
# variable-name= lambda parameters: "Even" if a%2==0 else "Odd"
    
addNum= lambda a,b: a+b 
print(addNum(2,3))

oddEven= lambda a: "Even" if a%2==0 else "Odd"
print(oddEven(22))
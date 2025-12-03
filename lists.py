# # Predefined Data Structures- list, tuple, sets, dictionary 
# # list - [], indexed, ordered, mutable(can change), heterogenous(multiple datatypes data store ho skta hai)

# # l=[34,22,'hello',True,5.67,100]
# # print(l)
# # print(type(l))
    
# # # list slicing 
# # print(l[2])
# # print(len(l))

# # print(l[:]) # start stop step
# # print(l[:3]) # start stop step
# # print(l[1:3]) # start stop step
# # print(l[1:5]) # start stop step
# # print(l[1:5:2]) # start stop step


# # # methods - 
# # l1=[23,45,11,10,40]
# # # l1.sort() # numeric
# # print(l1)

# # # append , extend 
# # l1.append(100)
# # print(l1)
# # l1.append([100,55,15])
# # print(l1)
# # print(l1[6][1])


# # # extend 
# # l1.extend([19,44,32])
# # print(l1)

# l=[34,33,21,199,23,67,76,55,39]
# print(l)

# # sort list 
# # l.sort()
# # print(l)

# # l.remove(23)
# # print(l)
# # Remove first occurrence of value.
# # Raises ValueError if the value is not present

# # l.pop()
# # l.pop(5)
# # print(l)

# l.insert(3,100)
# print(l)

# # l.clear()
# # print(l)

# print(l.index(23))
# print(l.count(23))



# for loop in list 

j=[34,32,11,100,67,99]

new=[]
for i in j:
    # print(i+2)
    # new.extend([i+2])
    new.append(i+2)
    
print(new)

# zip function 
a=[1,2,3,4]
b=[9,7,6,5,8]

# for i in zip(a,b):
#     print(i)
for i,j in zip(a,b):
    print(i,j)

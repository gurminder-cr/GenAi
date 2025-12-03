# dictionary is a heterogenours data structure, {}, key:value ke pair hotte hai, 

dict1={'name':'Anurag','class':'btech','rollno':123, 'IsPassout':True}
print(dict1)
print(type(dict1))

# methods 

# print(dict1['name'])
# print(dict1['names'])
# print(dict1.get('nameee','key not present')) 
# print("hello")

print(dict1)

# add 
dict1['marks']=97
print(dict1)

# dictionary update function 
dict1.update(hobby='playing cricket')
print(dict1)

# value update krrni ho 
dict1['rollno']=1123 
print(dict1)

# 
dict1.pop('rollno')  #mention key here , if key is not present then it raises a keyerror  
print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())


# for loop on dictionary 
# for i in dict1.items():
#     print(i)
# for i,j in dict1.items():
#     print(i,"=",j)

# dict1.clear()
# print(dict1)

# sets - {}, dictionary - {}
a={} # empty dictionary 
print(type(a))


s=set()
print(type(s))

dict2={
    'name':{
        'first':'Anurag',
        'last':'thakur'
    },
    'address':{
        'permanent':'HP',
        'temp':'Mohali'
    },
    'rollno':1234
}

print(dict2)

print(dict2['address']['temp'])


# enumerate function 

l=[13,44,31,44,567]

# for i in range(0,len(l)):
#     print(i,l[i])

# for i,j in enumerate(l):
#     print(i,j)
    
    
for i,j in enumerate(dict1.items()):
    print(i,"--",j)
    

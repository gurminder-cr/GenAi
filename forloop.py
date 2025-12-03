# range()

# for i in range(0,10): #start, stop - stop-1(-1 loop challegi)
#     print(i)
    
# for j in range(5): # by default starting point is 0 
#     print(j) 

# for j in range(3,13):
#     print('Anurag',j)

# reverse - step 
# for i in range(10,1,-2):  # stop-1 =1-(-1) = 2
#     print(i)
    
# for i in range(0,15,2):
#     print(i)
# for i in range(0,16,3):
#     print(i)
    
for i in range(1,40):
    if i%4==0:
        print(i)

num= int(input('enter num '))

for i in range(1,num):
    print(i)

# 
# naam='gurminder'
# print(len(naam))

# naam length - utni baar hi aapka naam print honna chahiye 


# nested for loop 
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()
        



# 1
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
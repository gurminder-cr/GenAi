#strings ' ', " "

naam='Anurag Thakur'
# print(naam)
# print(type(naam))

# # string methods
# print(naam.lower())
# print(naam.upper())
# print(naam.capitalize())
# print(naam.title())
# print(naam.swapcase())

# # condition based methods - True or False
# print(naam.startswith('Anu'))
# print(naam.endswith('r'))


# # replace 
# print(naam.replace('ra','dee')) # old string, new string 
# # if the old string is not present then it will return same value

# # 
# # check count and index  
# print(naam.count('r'))
# print(naam.index('a'))

# # find index of letter 
# print(naam.find('ra'))


# # strip - remove spaces 
# print("-------------------")
# print("-------------------")
# new_str="     dgsfsd      dhfs      "
# print(new_str.strip())
# print(new_str.lstrip())
# print(new_str.rstrip())

# print(new_str.replace('      ','_'))


# # split 
# text='hello, how are you'
# print(text.split(','))
# print(text.split('o'))


# # slicing
naam='Anurag Thakur' 
print(naam)

print(naam[6])
print(naam[:5]) # start stop step 
print(naam[1:8])
print(naam[2:])
print(naam[:10])
print(naam[::2])
print(naam[::-1]) # reverse
print(naam[8:1:-1]) # reverse


# for loop 

# for i in naam:
#     print(i, end='_')
    
s='mnbfhdsfs33'   
print(s.isalpha())
n='32435345'
print(n.isalnum())


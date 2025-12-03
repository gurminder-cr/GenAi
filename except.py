# exception handling - errors handle - syntax error, logical errors

# a=int(input("Enter a "))
# b=int(input("Enter b "))

# # print(a/b)

# l=[12,45,33,21,10]

# try:
#     print(a/b)
#     print(l[7])
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as i:
#     print(i)
# # except Exception as e:
# #     print(e)
# finally:
#     print("Always challega")

# print("hello")



# recursion 

def driving():
    age=int(input("Enter age "))
    if age<18:
        print("Cannot drive")
    else:
        if age>100:
            print("Age not valid please re-enter your age")
            driving()
        else:
            print("Can Drive")
driving()


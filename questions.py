
print(45/7)  # simple division 
print(45//7) # floor division 

# a=1
# while a<40:
#     print(a)
#     a=a+1
    
def nikhil(func):
    def wrapper():
        func()
        print("Before calling the function.")
        print("After calling the function.")
    return wrapper

@nikhil # Applying the decorator to a function
def greet():
    print("Hello,")
    
greet()


a=[12,45,76,10]
it= iter(a)
# print(it)
# print(list(it))
print(next(it)) #Return the next item from the iterator.
print(next(it))
print(next(it))




# generators - function mei se multiple values return laini hai to yield use hogga 
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
print(ctr)
print(list(ctr))
# print(next(ctr))
# print(next(ctr))
# for n in ctr:
#     print(n)
# sets - {} 

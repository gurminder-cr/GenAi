# file handling text files 

# read, write, append, create , r+w, w+r, seek(cursor point:location kahha prr hai)

# f= open('file.text','r') # r means read operation
# print(f.read())
# f.close()


# f=open('file.text','w') # w write
# f.write('hello')
# f.close()

# with open('file.text','a') as f:
#     f.write('Ansh')
# with open('file.text','w') as f:
#     f.write('Ansh')


# with open('file.text','r+') as f:
#     print(f.read())
#     f.seek(1)
#     f.write('Gurminder')
# with open('file.text','w+') as f:
#     f.write('Gurminder')
#     f.seek(0)
#     print(f.read())
    
    
# with open('new.text','x') as s:   #create and write 
#     s.write('hello')


# OS- operating system 

import os 
# os.makedirs('folder')
print(os.getcwd())
os.chdir('folder')
print(os.getcwd())

# for i in range(10,100):
#     os.makedirs(f'file{i}')

# for i in range(0,100):
#     os.removedirs(f'file{i}')



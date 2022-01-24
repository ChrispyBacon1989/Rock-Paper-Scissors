import datetime
import io
import os

fruits = ['apple','pear','strawberry','rasberry','orange', 'lemon','apple','pear','orange']
print(fruits.count('apple'))

#dictionaries are similar to arrays and lists but can store multiple sets of data per entry 
knights = {'gallahad':'the pure', 'robin':'the brave'}
for k, v in knights.items():
    print(k + ' ' + v)

#example of importing a function, in this case date and time
x = datetime.datetime.now()
print(x)

#opening a file and reading it to terminal
file = io.open("sample.txt",buffering =5)
print(file.read())
file.close()

#creating a folder/file
#os.name
#os.mkdir("F:\\test\tmp")
#os.chdir("F:\\test\tmp")
#os.
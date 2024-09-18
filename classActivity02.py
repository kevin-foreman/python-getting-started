import sys
import os

''' My file 1 '''
print('Opening file myfile1.txt.')
f = open('myfile1.txt')  # create file object

print('Reading file myfile1.txt.')
contents = f.read()  # read file text into a string

print('Closing file myfile1.txt.')
f.close()  # close the file

print('\nContents of myfile1.txt:\n', contents)

''' My file 2 '''
print('Opening file myfile2.txt.')
f = open('myfile2.txt')  # create file object

print('Reading file myfile2.txt.')
contents = f.read()  # read file text into a string

print('Closing file myfile2.txt.')
f.close()  # close the file

print('\nContents of myfile2.txt:\n', contents)

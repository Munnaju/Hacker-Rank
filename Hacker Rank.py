#!/usr/bin/env python
# coding: utf-8

# In[16]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())

print (a//b, float(a/b), sep='\n')


# In[18]:


if __name__ == '__main__':
    n = int(input())

for a in range(0, n):
    print(a ** 2)


# In[2]:


import math
import os
import random
import re
import sys


# In[2]:


if __name__ == '__main__':
    n = int(input().strip())
    
if n % 2 != 0:
    
    print ('Weird')
    
else:
    if n>= 2 and n <=5:
        print ('Not Weird')
    elif n>=6 and n<=20:
        print ('Weird')
    elif n>20:
        print ('Not Weird')


# In[32]:


import sys


N = int(input().strip())

if N % 2 != 0:
    print ("Weird")
else:
    if N >= 2 and N <= 5:
        print ("Not Weird")
    elif N >= 6 and N <= 20:
        print ("Weird")
    elif N > 20:
        print ("Not Weird")


# In[2]:


def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 != 0:
            leap = True
        elif year % 400 == 0:
            leap = True
    return leap


year = int(input())


# # Read an integer.
# 
# Without using any string methods, try to print the following:
# 
# Note that "..." represents the values in between.
# 

# In[4]:


if __name__ == '__main__':
    n = int(input())

    for n in range (1,n+1):
        print (n, end = '')


# In[ ]:


##Second Runner up

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

new_list= []

for i in arr:
    if i not in new_list:
        new_list.append(i)
    
new_list.sort(reverse=True)
print (new_list[1])


# 

# # Nested List
# 
# #Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# In[11]:


score_list = []
mark_sheet = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    mark_sheet.append([name,score])
    score_list.append(score)


second_lowest_mark = sorted(list(dict.fromkeys(score_list)))[1]

for name,marks in sorted(mark_sheet):
    if marks == second_lowest_mark:
        print(name)


# In[9]:


#List Iteration

my_pets = ['cat', 'dog', 'rabbit']
uppered_pets = []

for pet in my_pets:
    pets_ = pet.upper()
    uppered_pets.append(pets_)
    
print (uppered_pets)
    


# In[12]:


#Map function

my_pets = ['cat', 'dog', 'rabbit']
uppered_pets = list(map(str.upper, my_pets))

print (uppered_pets)


# In[7]:


#Append method revision

animals = ['cat', 'dog', 'rabbit']
animals.append('guinea pig')
print('Updated animals list: ', animals)


# # Finding the percentage
# 
# You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer N followed by the names and marks for N students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

# In[21]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        scores=sum(scores)/3
        student_marks[name] = scores
    query_name = input()
    print('%.2f' % student_marks[query_name])


# # Tuples
# 
# Given an integer,n, and n-space separated integers as input, create a tuple t, of those n integers. Then compute and print the result of hash (t)

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print (hash(t))


# # List

# In[1]:


if __name__ == '__main__':
    N = int(input())
    result = []
    for n in range(N):
        x = input().split(" ")
        command = x[0]
        if command == 'append':
            result.append(int(x[1]))
        if command == 'print':
            print(result)
        if command == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if command == 'reverse':
            result = result[::-1]
        if command == 'pop':
            result.pop()
        if command == 'sort':
            result = sorted(result)
        if command == 'remove':
            result.remove(int(x[1]))


# In[1]:


language = ['english', 'hindi', 'urdu', 'panjabi']
language.pop(0)
language[::-1]


# In[6]:


#HackerRank.com presents "Pythonist 2".
#hACKERrANK.COM PRESENTS "pYTHONIST 2".


def swap_case(s):
    return s.swapcase()

#if __name__ == '__main__':


# In[17]:


line = 'HackerRank.com presents Pythonist 2'
for words in line:
    new_line = line.split()
    ''.join(map(lambda s: s[:-1]+ s[-1].upper(),s.title().split()))
    
print(new_line)


# In[ ]:





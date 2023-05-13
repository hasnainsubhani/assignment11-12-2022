#!/usr/bin/env python
# coding: utf-8

# Question 1:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# In[ ]:


class Iter:
    def __init__(self):
        pass
        
    def divid(self,n):
        for i in range(0,n):
            if i%7==0:
                yield i


# Question 2:
# Write a program to compute the frequency of the words from the input. The output
# should output after sorting the key alphanumerically.

# In[ ]:


import operator

text_line = input("Please enter the sentence: ")

freq_dict = {}

for i in text_line.split(' '):
    if i.isalpha():
        if i not in freq_dict:
            freq_dict[i] = 1
        elif i in freq_dict:
            freq_dict[i] = freq_dict[i] + 1
    else:
        pass

sorted_freq_dict = sorted(freq_dict.items(), key = operator.itemgetter(0))
print(sorted_freq_dict)

for i in sorted_freq_dict:
    print(i[0], i[1])


# In[ ]:





# Question 3:
# 
# Define a class Person and its two child classes: Male and Female. All classes have a
# method "getGender" which can print "Male" for Male class and "Female" for Female
# class.

# In[ ]:


class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print(aMale.getGender())
print(aFemale.getGender())


# Question 4:
# Please write a program to generate all sentences where subject is in ["I", "You"] and
# verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

# In[2]:


subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentence)


# Question 5:
# Please write a program to compress and decompress the string "hello world!hello
# world!hello world!hello world!".

# In[6]:


import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(bytes(s, 'utf-8'))
print(t)
print(zlib.decompress(t))


# Question 6:
# Please write a binary search function which searches an item in a sorted list. The
# function should return the index of element to be searched in the list.

# In[ ]:





# In[ ]:





# In[ ]:





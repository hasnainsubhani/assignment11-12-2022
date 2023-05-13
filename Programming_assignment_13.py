#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1:
    
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated
sequence.


# In[9]:


import math
numbers = input("please enter comma-separated sequence.").split(',')
C = 50 
H = 30
result=[]

for i in range(0,len(numbers)):
    numb = numbers[i]
    result.append(str(int(math.sqrt((2 * C * int(numb))/H))))
    
print(','.join(result))
    


# Question 2:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
# element value in the i-th row and j-th column of the array should be i*j.

# In[11]:


m=int(input("ENTER THE ROWS : "))
n=int(input("ENTER THE COLUMNS : "))

for i in range(0,m):
     for j in range(0,n):
         print(i*j,end="  ")
     print("\n")


# In[ ]:


Question 3:
Write a program that accepts a comma separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically.


# In[13]:


items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))


# In[ ]:


Question 4:
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.


# In[14]:


from collections import Counter
 
def remov_duplicates(input):
    input = input.split(" ")
    UniqW = Counter(input)
    s = " ".join(UniqW.keys())
    print (s)


# In[15]:


remov_duplicates('Python is great and Java is also great')


# In[ ]:


Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.


# In[16]:


alpha,string=0,"asrdw1234"
for i in string:
    if (i.isalpha()):
        alpha+=1
print("Number of Digit is", len(string)-alpha)
print("Number of Alphabets is", alpha)


# In[ ]:


Question 6:
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.


# In[17]:


l, u, p, d = 0, 0, 0, 0
s = "R@m@_f0rtu9e$"
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="$@_"
digits="0123456789"
if (len(s) >= 8):
    for i in s:
 
        # counting lowercase alphabets
        if (i in smallalphabets):
            l+=1           
 
        # counting uppercase alphabets
        if (i in capitalalphabets):
            u+=1           
 
        # counting digits
        if (i in digits):
            d+=1           
 
        # counting the mentioned special characters
        if(i in specialchar):
            p+=1       
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
    print("Valid Password")
else:
    print("Invalid Password")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to find words which are greater than given length k?

# In[2]:


def string_k(k, str):
    string = []
    text = str.split(" ")
    for x in text:
        if len(x) > k:
            string.append(x)
    return string


# 2. Write a Python program for removing i-th character from a string?

# In[4]:


def remove(string, i):
    a = string[: i]
    b = string[i + 1:]
    return a + b


# 3. Write a Python program to split and join a string?

# In[ ]:


def split_string(string):
    list_string = string.split(' ')
    return list_string
 
def join_string(list_string):
    string = '-'.join(list_string)
    return string


# 4. Write a Python to check if a given string is binary string or not?

# In[ ]:


def binary_check(string):
    p = set(string)
 
    # declare set of '0', '1' .
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        print("No")


# 5. Write a Python program to find uncommon words from two Strings?

# In[ ]:


def UncommonWords(w1, w2):
    w1=w1.split()
    w2=w2.split()
    x=[]
    for i in w1:
        if i not in w2:
            x.append(i)
    for i in w2:
        if i not in w1:
            x.append(i)
    x=list(set(x))
    return x


# 6. Write a Python to find all duplicate characters in string?

# In[ ]:


def find_duplicate_char(input):
    WC = Counter(input)
    for letter, count in WC.items():
        if (count > 1):
            print(letter)


# 7. Write a Python Program to check if a string contains any special character?

# In[ ]:


def special character_check(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(string) == None):
        print("String is accepted")
         
    else:
        print("String is not accepted.")


# In[ ]:





# In[ ]:





# In[ ]:





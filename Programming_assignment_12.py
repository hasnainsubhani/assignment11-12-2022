#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('pinfo', 'values')


# In[ ]:


_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}

res = list(sorted({ele for val in test_dict.values() for ele in val}))
print("The unique values list is : " + str(res))


# 2. Write a Python program to find the sum of all items in a dictionary?

# In[ ]:


def _sum(myDict):
 
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
 
    return final
 


# 3. Write a Python program to Merging two Dictionaries?

# In[ ]:


def _merge(dict1, dict2):
    return(dict2.update(dict1))


# 4. Write a Python program to convert key-values list to flat dictionary?

# In[1]:


test_dict = {'month' : [1, 2, 3],
            'name' : ['Jan', 'Feb', 'March']}
x=list(test_dict.values())
a=x[0]
b=x[1]
d=dict()
for i in range(0,len(a)):
    d[a[i]]=b[i]
# printing result
print("Flattened dictionary : " + str(d))


# 5. Write a Python program to insertion at the beginning in OrderedDict?

# In[ ]:


initial_dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
initial_dict2 = OrderedDict([("manjeet", '4'), ("akash", '4')])

both = OrderedDict(list(initial_dict2.items()) + list(initial_dict1.items()))
print ("Final Dictionary :"+str(both))


# 6. Write a Python program to check order of character in string using OrderedDict()?

# In[ ]:


from collections import OrderedDict
 
def checkOrder(input, pattern):
    dict = OrderedDict.fromkeys(input)
    ptrlen = 0
    for key,value in dict.items():
        if (key == pattern[ptrlen]):
            ptrlen = ptrlen + 1
         
        if (ptrlen == (len(pattern))):
            return 'true'
 
    return 'false'


# 7. Write a Python program to sort Python Dictionaries by Key or Value?

# In[ ]:


myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
 
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
 
print(sorted_dict)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





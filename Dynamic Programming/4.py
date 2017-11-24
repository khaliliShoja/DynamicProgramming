
# coding: utf-8

# Say you have an array for which the ith element is the price of a given stock on day i, if you were only permitted to complete at most one transaction, design for finding the maximum profit.
# 

# In[8]:




l=[7,1,5,3,6,4]


def calMax(n,l):
  s=[0]*n
  s[0]=0
  for i in range(1,n):
    maxx=s[i-1]
    for j in range(0,i):
      if(l[i]-l[j] >= maxx):
        s[i]=l[i]-l[j]
        maxx=s[i]
      else:
        s[i]=maxx
  return s



print(calMax(len(l),l))
  
  


# In[ ]:




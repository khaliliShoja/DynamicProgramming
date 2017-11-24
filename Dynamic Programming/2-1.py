
# coding: utf-8

# Given a road of length n and pairs p[i] for i=1,2,3,... where p[i] is the price of a rod of length i. Find the maximum total revenue you can make by cutting and selling the rod.

# In[4]:


def calmax(n,p):
  s=[0]*(n+1)
  s[1]=p[1]
  for i in range(2,n+1):
    maxx=-1
    for j in range(0,i):
      a=s[j]+p[i-j]
      if(a > maxx):
        maxx=a
    s[i]=maxx
  return s




p=[0,1,5,8,9,10]

print(calmax(5,p))


# In[ ]:




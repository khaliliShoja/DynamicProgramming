
# coding: utf-8

# Given a road of length n and pairs p[i] for i=1,2,3,... where p[i] is the price of a rod of length i. Find the maximum total revenue you can make by cutting and selling the rod.

# In[3]:

def calmax(n, p):
  if(n==0):
    return 0
  if(n==1):
    return p[1]
  
  maxx=-1
  
  for i in range(1,n+1):
    a=p[i]+calmax(n-i, p)
    if(a > maxx):
      maxx=a
      
  return maxx



p=[0,1,5,8,9,10]

print(calmax(5,p))


# In[ ]:




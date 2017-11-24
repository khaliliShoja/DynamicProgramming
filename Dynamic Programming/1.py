
# coding: utf-8

# You can climb 1 or 2 stairs with one step. How many different ways can you climb n stairs?

# In[1]:

def climbSt(n):
  s=[0]*(n+1)
  s[0]=0
  s[1]=1
  s[2]=2
  
  for i in range(3,n+1):
    s[i]=s[i-1]+s[i-2]
    #print(s)
  return s
  
s=climbSt(4)
print(s)


# In[ ]:




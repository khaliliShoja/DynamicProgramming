
# coding: utf-8

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# In[2]:

p=[0,1,2,3,4,5]
p=[0,0,10,0,0,10]
def calMax(n,p):
  s=[0]*(n+1)
  s[0]=0
  s[1]=p[1]
  
  for i in range(2,n+1):
    #maxx=-1
    if(i==2):
      if(s[i-1]>p[i]):
        s[i]=s[i-1]
      else:
        s[i]=p[i]
    else:
      if(s[i-1] > s[i-2]+p[i]):
        s[i]=s[i-1]
      else:
        s[i]=s[i-2]+p[i]
  return s
  
  
print(calMax(5,p))
        


# In[ ]:




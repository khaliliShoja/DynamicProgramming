
# coding: utf-8

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# In[1]:

p=[0,1,2,3,4,5]
p=[0,0,10,0,0,10]
l=[0,-1,-1,-1,-1,-1]


def calMax(l, p, s):
  n=len(p)-1
  if(-1 not in l):
    #print(s[0])
    return s[0]
  
  
  
  a1=0
  a2=0
  maxx=-9
  for i in range(1,n+1):
    maxx1=-9

    if(l[i]==-1):
      if(i!= n and  l[i-1]!=1 and l[i+1]!=1):
        l1=l[:]
        l1[i]=1
        s1=s[:]
        s1[0]=s1[0]+p[i]
        #print(s1)
        a1=calMax(l1,p,s1)
      if(i==n and l[i-1]!=1):
        l1=l[:]
        l1[i]=1
        s1=s[:]
        s1[0]=s1[0]+p[i]
        #print(s1[0])
        a1=calMax(l1,p,s1)
        #print(a1)
      
      l2=l[:]
      l2[i]=0
      s2=s[:]
      a2=calMax(l2,p,s2)
      #print(a2)
    if(a1 > a2):
      maxx1=a1
    else:
      maxx1=a2
  if(maxx1>maxx):
    return maxx1
  else:
    return maxx


print(calMax(l,p,[0]))
    


# In[ ]:




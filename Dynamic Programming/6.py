
# coding: utf-8

# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
# 

# In[10]:

v=[0,30,14,16,9]
w=[0,6,3,4,2]
#Total weight is 10
tw=10
def maxVal(tw,v,w):
  m=[[0]*(tw+1) for i in range (0,len(v))]
  for i in range(0,len(v)):
    for j in range(0, tw+1):
      if(i==0 or j==0):
        m[i][j]=0
      else:
        if(j >= w[i]):
          if(m[i-1][j] > m[i-1][j-w[i]]+v[i]):
            m[i][j]=m[i-1][j]
          else:
            m[i][j]=m[i-1][j-w[i]]+v[i]
        else:
          m[i][j]=m[i-1][j]
  return m
print( maxVal(tw,v,w))
          
  


# In[ ]:




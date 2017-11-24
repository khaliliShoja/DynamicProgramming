
# coding: utf-8

# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
# 
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.
# 
# Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.
# 

# In[9]:


l=[[1,2],[2,3],[3,4]]



l.sort(key=lambda x:x[1], reverse=True)
#print(l)
#print(l[0][0])

def calMax(l):
  
  s=[0]*len(l)
  s[0]=1
  
  for i in range(1,len(l)):
    
    maxx=1
    for j in range(0,i):
      
      if(l[j][0]> l[i][1]):
        s[i]=s[j]+1
        #print(s[i])
        if(maxx < s[i]):
          maxx=s[i]
    s[i]=maxx
  
  return s
      


print(calMax(l))  
  


# In[ ]:




import numpy as np

n = 3

x = [[0]*n]*n

def posProvider(i,j)->list:
    if i==-2 and j==-2:
        return [n//2,n-1]
    
    i = i-1
    j = j+1
    
    if j==n:
        j=0
    if i==n:
        i=0
    
    if x[i][j] !=0:
        j-=2
        i+=1
    
    if i==-1:
        if j==n:
            i=0
            j=n-2
        else:
            i=n-1
            
    return[i,j]
    

i=-2
j=-2

x = np.array(x)

for k in range(1,(n**2)+1):
    pos = posProvider(i, j)
    i = pos[0]
    j = pos[1]
    
    x[i][j]=k
    
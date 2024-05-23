x = [1,2,3,4,5,6,7,8,9]

i=0
while i!=len(x)-2:
    a = x[i]
    b = x[i+1]
    c = x[i+2]
    
    if (a>b and b>c) or (a<b and b<c):
        x[i+1] = c
        x[i+2] = b
    
    i+=1
    
    
import matplotlib.pyplot as plt

plt.plot(range(len(x)),x)
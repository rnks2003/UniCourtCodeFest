x = [3,0,2,0,4]

temp = 0
sum = 0
i=0

while max(x)!=0:
    if x[i]>0:
        x[i]-=1
        for j in range(i+1,len(x)):
            if x[j]==0:
                temp+=1
            if x[j]>0:
                x[j]-=1
                sum+=temp
                temp=0
        i=0
    else:
        i=0
        while x[i]==0:
            i+=1
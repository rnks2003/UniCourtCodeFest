x = [5,5,10,100,10,5]
#x = [3,2,5,10,7]
y = []

sum = 0

for i in range(len(x)):
    a = x[i]
    b = x[i+1]
    c = x[i+2]
    
    j = max(a,b,c)
    
    if j==c and i!= len(x)-3:
        if c>x[i+3]+b :
            if j not in y or (b in y and x.count(b)>1):
                sum+=j
                y.append(j)
        else:
            k = max(a,b)
            if k not in y or (b in y and x.count(b)>1):
                sum+=k
                y.append(k)
        continue
            
    if j==b:
        if i+3<len(x):
            if b+x[i+3] > a+c :
                if b not in y or (b in y and x.count(b)>1):
                    sum+=b
                    y.append(b)
    
    if j==a:
        if (x[i-1] not in y) and( (a not in y) or (a in y and x.count(a)>1) ):
            sum+=a
            y.append(a)
     
    if i == len(x)-3:
        if x[i] in y:
            sum+=x[len(x)-1]
        else:
            sum+=max(b,c)
        break
                
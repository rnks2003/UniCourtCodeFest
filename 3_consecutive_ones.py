n = 4

bins = []

for i in range(2**n):
    num = bin(i)[2:]
        
    if len(num)<3 and num!='11' :
        bins.append(num)
    elif len(num)>=3:
        if len(num)==3:
            if num[0]!=num[1]:
                bins.append(num)
        
        else:
            a = num[0]
            flag=True
            for j in range(1,len(num)):
                b =num[j]
                if a == '1' and b == '1':
                    flag = False
                else:
                    a = num[j]
            if flag:
                bins.append(num)
            
res = len(bins)
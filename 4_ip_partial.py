ip = "192168112169"
res = ""


if len(ip)<4 or len(ip)>12:
    res = "-1"
    
elif len(ip)==4:
    for i in ip:
        res = res+i+'.'
    res = res[:-1]
    
elif len(ip)==12:
    for i in range(0,12,3):
        a = ip[i]+ip[i+1]+ip[i+2]
        a = int(a)
        if a < 256:
            res = res+str(a)
            res+='.'
        else:
            res = '-1 '
            break
    res = res[:-1]
    
        
else:
    i=0
    while i<len(ip)-2:
        a = ip[i]+ip[i+1]+ip[i+2]
        a = int(a)
        if a < 256:
            res = res+str(a)
            res+='.'
            i+=3
        else:
            a = ip[i]+ip[i+1]
            a = int(a)
            res = res+str(a)
            res+='.'
            i+=2
    res = res[:-1]
    if(len(res)!=len(ip)+3):
        res="-1"
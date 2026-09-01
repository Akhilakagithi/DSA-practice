n=34021
p=1
while n>0:
    q=n//10
    #print(q)
    r=n%10
    if r==0:
        p=p*1
        n=q
    else:    
    #print(r)
        p=p*r
        n=q
print(p)

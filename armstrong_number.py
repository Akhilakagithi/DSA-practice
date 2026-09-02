n=153
original=n
cube=0
while n>0:
    r=n%10
    formula=r**3
    cube=cube+formula
     n=n//10
if original==cube:
    print("armstrong")
else:
    print("not armstrong numnber")

def calc3(x,y,z):
    a=(x*y*z)/3
    return(a)
x=0
for i in range(0,5):
    x += calc3(i,3,6)

if(x<100):
    print("OK")
else:
    print("NG")
    
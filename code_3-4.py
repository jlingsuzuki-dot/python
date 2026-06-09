def calc3(x,y,z):
    a = (x*y*z)/3
    return(a)

a = [3,5,9,10]
x = 0
for i in range(0,4):
    b = a[i]
    x += calc3(b,3,6)

print(x)
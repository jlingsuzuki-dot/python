def calc_tax(a):
    r=1.1
    x=a*r
    return(x)

goods = [1000,2000,3000]
total = 0

for i in range(0,len(goods)):
    total += goods[i]

total = calc_tax(total)
print(int (total))
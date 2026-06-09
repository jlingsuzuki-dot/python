def calc_tax(a):
    r=1.1
    x=a*r
    return(x)

goods = []
goods.append(1000)
goods.append(2000)
goods.append(3000)
goods.append(4000)
total = 0

for i in range(0,len(goods)):
    total += calc_tax(goods[i])

print(int(total))
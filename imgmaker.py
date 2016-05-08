from random import randint
import math

f=open('image.ppm','w')
f.write('P3 500 500 255')
r=0
g=0
b=0
for i in range(500):
    for j in range(500):
        if j>250:
            r=math.hypot(i%9, j)
        else:
            r=math.hypot(math.sqrt((i*i)+(j*j)), 0)
        if j<=i:
            g=i/4
            b=j/4
        elif j<=(500-i):
            g=i/6
            b=i/6
        else:
            g=i*.5
            b=j*.5
        #b=math.sqrt((i*i)+(j*j))
        s=' %d %d %d' % (r,g,b)
        f.write(s)
f.close()

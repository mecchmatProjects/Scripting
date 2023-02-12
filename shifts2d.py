from math import sqrt

plist = input().split()
x = plist[::2]
y = plist[1::2]

def shift2d(p,x0,y0,h):
    p1 = p[1:] + [p[0]]
    #y1 = y[1:] + [y[0]] 
    ans = []
    for pp,pn in zip(p,p1):
        x1,y1 = pp
        x2,y2 = pn
        hi = ((y2-y1) * x0 + (x2-x1) * y0 )/sqrt((x2-x1)**2 + (y2-y1)**2)
        z1 = (hi-h) * x1 /h
        t1 = (hi-h) * y1 /h
        ans.append(z1)
        ans.append(t1)
    return ans    






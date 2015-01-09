def pentl(n):
    penl=(n*(3*n-1))//2
    return(penl)

def ass(n):
    for b in range(2,n):
        sum = pentl(n) + pentl(b)
        diff = pentl(n) - pentl(b)
        if petd(sum,n): 
            if petd(diff,n):
                global a
                a=1
                print(diff)
    


def petd(c,n):
    if c > pentl(n):
        while c >= pentl(n):
            if pentl(n) == c:
                return(True)
            n += 1
        return(False)
    while c <= pentl(n):
        if pentl(n) == c:
            return(True)
        n -= 1
    return(False)
    
    



def petc(c,n):
    t=1
    a=pentl(n+1)
    if c > a:
        for t in range(1,c):
            c -= (3*(n+1) +1)
            if c == a:
                return(True)
        return(False)
    for t in range(1,c):
        c += (3*t +1)
        if c  ==a:
            return(True)
    return(False)
#print(pentl(15))
#print(petd(92,15))

    
global a
a=0
n = 1
while a == 0:
    ass(n)
    n += 1

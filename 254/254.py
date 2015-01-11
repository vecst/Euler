from _functools import reduce
import operator

def fact(n):
    """find factorial"""
    return(reduce(operator.mul,range(1,n+1),1))

def f(n):
    """change integer to string and feed it to factorial and sum it"""
    return sum(map(lambda x:fact(int(x)),str(n)))

def s(n):
    """summing the digits of an integer"""
    return(sum(map(lambda x:int(x),str(n))))

def neighger(n):
    i=1
    a=list(range(1,n+1))
    zum=0
    while len(a) > 0:
        sg = s(f(i))
        if sg in a:      
            a.remove(sg)
            zum +=(s(i))
        i += 1
    return(zum)

print(neighger(150))

from _functools import reduce
import operator

def fact(n):
    """find factorial"""
    return(reduce(operator.mul,range(1,n+1),1))

def splits(n):
    """change integer to string and feed it to factorial and sum it"""
    return(sfa(sum(map(lambda x:fact(int(x)),str(n)))))


def sfa(n):
    """summing the digits of an integer"""
    return(sum(map(lambda x:int(x),str(n))))
def goi(n):
    a=1
    """g of i the smallest positive integer such that sfa(n)=i"""
    while True:
        if splits(a) == n:
            break
        a += 1
        if a > 100000:
            a *= 11//3
    return a


def black(n):
    lzt = []    
    for b in range(1,15):
        print(splits(b), end='splits \n')
        a = sfa(goi(b))
        lzt.append(a)
        
    print(sum(lzt))
black(1)
print(splits(5232))
# def sigmass(tit):
#     """makes and searches from lists to make the sum of a  list"""
#     lzt=[]
#     n=1
#     i=1
#     lzt2 =[]
#     zum = 0
#     found = 0
#     for i in range(1, tit+1):

#         try:
#            found = lzt.index(i)
#            print(i)
#         except ValueError:
#            z=0
#            while z != i:
#                z = splits(n)
#                lzt.append(z)
#                n += 1
#            found = n
#         zum += sfa(found)
#     return zum
# print(sigmass(150))

# def test(n):
#     z=0
#     """test for 47"""
#     while z != 10:
#         z = splits(n)
#         print(z)
#         n += 1
#     return z,n-1
# print(test(1))
# print(splits(47))

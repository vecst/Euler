## project 31 I think
def lbs(q):
    a=1
    b=2
    c=5
    d=10
    e=20
    f=50
    g=100
    h=200
    z=0

    for i in range(0, 200*q):
        for j in range(0, 200*q):
            for k in range (0, 200*q):
                for l in range(0, 200*q):
                    for m in range(0, 200*q):
                        for n in range(0, 200*q):
                            for o in range(0, 200*q):
                                for p in range(0, 200*q):
                                    if a*i + b*j + c*k + d*l + e *m +f*n + g*o + p*h == 200:
                                        z +=1
                                        print(z)

            
    
lbs(1)

def main(maxx):

    def seq(n):
        lzt = []
        i = 0
        while maxx >= n*i:
            lzt.append(n*i)
            i += 1
        return lzt

    z = 0
    for a in seq(1):
        for b in seq(2):
            for c in seq(5):
                for d in seq(10):
                    for e in seq(20):
                        for f in seq(50):
                            for g in seq(100):
                                for h in seq(200):
                                    if a+b+c+d+e+f+g+h == maxx:
                                        z += 1

    print("Final answer: "),
    print(z)

main(200)

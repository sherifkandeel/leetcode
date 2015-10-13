import random

def sol1(a):
    maxx = -1
    a.sort()
    for i in range(len(a)-2):
        p = a[i]
        q = a[i+1]
        r = a[i+2]
        if p+q > r and p+r > q and r+q > p:
            if maxx == -1 or p+q+r < maxx:
                maxx= p+q+r
    return maxx
            

def sol2(a):
    maxx = -1
    a.sort()
    for i in range(len(a)):
        for j in range(i, len(a)):
            if i==j: continue
            for k in range(j, len(a)):
                if j == k: continue
                if a[i]+a[j] > a[k] and a[j]+a[k] > a[i] and a[i]+a[k] > a[j] :
                    if maxx == -1 or a[i]+a[j]+a[k] < maxx:
                        maxx = a[i]+a[j]+a[k]
    return maxx


def driver():
    false = 0
    for i in range(100):
        n = random.randint(3,100)
        arr = random.sample(range(3,100000), n)
        s1 = sol1(arr)
        s2 = sol2(arr)
        if s1 != s2:
            print arr, s1, s2
            input()
            false+=1
        # print "solution 1: %d, reference solution: %d, equality: %s"%(s1, s2, s1==s2)
    print "number of falses: %d"%false
driver()

            



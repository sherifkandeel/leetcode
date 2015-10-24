import random
# import sys
# print sys.getrecursionlimit()

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
                        # print a[i], a[j], a[k]
                        maxx = a[i]+a[j]+a[k]
    return maxx


# def minbinsearch(a, start, end, pq):
#     while start <= end:
#         middle = start + (end-start)/2
#         print a[middle]
#         if pq >= a[middle]:
#             end = middle + 1
#         else:
#             start = middle + 1

#     # print "final value"+a[end+1]
#     if end+1<len(a):
#         return a[end+1]
#     return a[end]

# def sol3(a):
#     a.sort()
#     for i in range(len(a)-1):
#         p = a[i]
#         q = a[i+1]
#         r = minbinsearch(a, 0, len(a)-1, p+q)
#         print p, q, r
#         if p+q> r and p+r>q and q+r>p:
#             return p+q+r
#     return -1



def driver():
    false = 0
    for i in range(100):
        n = random.randint(3,100)
        arr = random.sample(range(3,100000), n)
        s1 = sol2(arr)
        s2 = sol3(arr)
        if s1 != s2:
            # print arr, s1, s2
            # input()
            false+=1
        # print "solution 1: %d, reference solution: %d, equality: %s"%(s1, s2, s1==s2)
    print "number of falses: %d"%false
# driver()
print sol3([1,2,4,5,6,7,8,9])
print sol2([1,2,4,5,6,7,8,9])

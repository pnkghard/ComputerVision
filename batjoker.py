
try:
    t=int(input())
    for i in range(t):
        j=list(map(int,input().split()))
        n=j[0]
        m=j[1]
        l=j[2]

        a=[]
        for k in range(m):
            b=list(map(int,input().split()))
            a.append(b[1:])

        strip=list(map(int,input().split()))
        length=1

        ind = {}
        for x,g in enumerate(a):
            for e in g:
                ind.setdefault(e, set()).add(x)
        def same_group(e1,e2):
            return ind.get(e1, set()) & ind.get(e2, set())

        for y in range(len(strip)-1):
            if (same_group(strip[y],strip[y+1])==set()):
                length+=1       
        print(length)
except:
    pass



# Sample Input 1 
# 3
# 2 2 2
# 1 2
# 1 1
# 2 1
# 2 2 4
# 1 1
# 1 2
# 1 2 2 1
# 3 2 3
# 2 1 3
# 1 2
# 1 3 1
# Sample Output 1 
# 2
# 3
# 1

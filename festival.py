t = int(input())

for i in range(t):
    a = list(map(int, input().split(" ")))
    at = []
    for j in range(a[1]):
        b = list(map(int, input().split(" ")))
        at.append(b)
    
    b = a[2]
    sum = at[0][0] + at[b-1][0]
    print("Case #"+str(i+1)+": "+str(sum))
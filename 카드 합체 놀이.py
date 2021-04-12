n,m = map(int,input().split())
a = list(map(int,input().split()))
sum = 0
for _ in range(m) :
    a.sort()
    b = a[0] + a[1]
    a[0] = a[1] = b
for i in range(n) :
    sum += a[i]
print(sum)

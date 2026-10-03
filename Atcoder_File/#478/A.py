n, m = map(int,input().split())
a= [0]*n
j = 0
for i in range(m):
    a[i % n] += 1
for i in range(n):
    print(a[i])
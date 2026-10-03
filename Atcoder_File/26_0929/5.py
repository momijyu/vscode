n, y = map(int,input().split())
for i in range(n+1):
    for ii in range(n+1 -i):
        iii = n -i - ii
        if 10000*i + 5000*ii + 1000*iii == y and iii >= 0:
            print(i, ii, iii)
            exit()
print(-1, -1, -1)
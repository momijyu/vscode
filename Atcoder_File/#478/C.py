from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
p, q = deque(), deque()

b = []
for i in range(n - 1):
    if a[i] > a[i + 1]:
        b.append(i)
if not b:
    print("Yes")
    exit()
l, r = b[0], b[-1]

for j in range(k):
    while p and a[p[-1]] >= a[j]:
        p.pop()
    p.append(j)
    
    while q and a[q[-1]] <= a[j]:
        q.pop()
    q.append(j)

ans = False
for i in range(n - k + 1):
    if i <= l and r <= i + k - 2:
        mn, mx = a[p[0]], a[q[0]]
        
        ok_l = (i == 0) or (a[i - 1] <= mn)
        ok_r = (i + k == n) or (mx <= a[i + k])
        
        if ok_l and ok_r:
            ans = True
            break

    if i + k < n:
        if p and p[0] == i:
            p.popleft()
        if q and q[0] == i:
            q.popleft()

        nxt = i + k
        while p and a[p[-1]] >= a[nxt]:
            p.pop()
        p.append(nxt)

        while q and a[q[-1]] <= a[nxt]:
            q.pop()
        q.append(nxt)
if ans:
    print("Yes")
else:
    print("No")
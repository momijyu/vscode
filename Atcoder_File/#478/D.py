from collections import defaultdict

n, q = map(int, input().split())
dict = defaultdict(list)
for _ in range(q):
    l, r, x = map(int, input().split())
    dict[x].append((l, r))

imos = [0] * (n + 2)
#print(dict)
print(list(dict.items()))
for x, lis in dict.items():
    lis.sort()
    
    ran = []
    for l, r in lis:
        if not ran:
            ran.append([l, r])
        else:
            if l <= ran[-1][1]:
                ran[-1][1] = max(ran[-1][1], r)
            else:
                ran.append([l, r])

    for l, r in ran:
        imos[l] += 1
        imos[r + 1] -= 1
#print(imos)

ans = []
cnt = 0
for i in range(1, n + 1):
    cnt += imos[i]
    ans.append(cnt)

print(*ans)
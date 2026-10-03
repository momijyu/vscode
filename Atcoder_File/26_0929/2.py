k = int(input())
s = str(input())
if k >= len(s):
    print(s)
else:
    for i in range(k):
        print(s[i], end ="")
    print("...")
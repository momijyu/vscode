from collections import deque
s_t = deque()
s_f = deque()
state = True

s = str(input())
s_t.append(s)
s_f.append(s)

q = int(input())
for i in range(q):
    a = input().split()
    if a[0] == "1":
        state = not state
    elif a[0] == "2":
        if a[1] == "1":
            if state == True:
                s_t.append(a[2])
                s_f.appendleft(a[2])
            else:
                s_f.append(a[2])
                s_t.appendleft(a[2])
        else:
            if state == False:
                s_t.append(a[2])
                s_f.appendleft(a[2])
            else:
                s_f.append(a[2])
                s_t.appendleft(a[2])
if state == True:
    print(*s_t)
else:
    print(*s_f)
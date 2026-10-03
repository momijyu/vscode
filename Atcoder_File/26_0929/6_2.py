from collections import deque
st = deque()
state = True
s = deque(input())
q = int(input())
for i in range(q):
    a = input().split()
    if a[0] == "1":
        state = not state
    else:
        if a[1] == "1":
            if state:
                st.append(a[2])
            else:
                st.appendleft(a[2])
        if a[1] == "2":
            if state:
                st.appendleft(a[2])
            else:
                st.append(a[2])
print(st)
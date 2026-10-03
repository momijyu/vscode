n = int(input())
s_q = set()
s_nq = set()
s = []
for i in range(n):
    sa = str(input())
    s.append(sa)
#print(s)
for i in s:
    if i[0] == "!":
        s_q.add(i[1:])
        if i[1:] in s_nq:
            print(i[1:])
            exit()
    else:
        s_nq.add(i)
        if i in s_q:
            print(i)
            exit()
print("satisfiable")
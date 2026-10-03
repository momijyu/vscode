n = int(input())
s_q = set()
s_nq = set()
c = True
for i in range(n):
    s = str(input())
    if s[0] == "!":
        #print(111111,s[1:])
        s_q.add(s[1:])
    else:
        s_nq.add(s)
    if s_nq & s_q and c:
        c = False
        print(*(s_q & s_nq))
if c == True:
    print("satisfiable")
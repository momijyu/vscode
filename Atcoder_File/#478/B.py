def ra(n, v, w,ssum= 0, psum= 0, i = 1, cnt = 0):
    if cnt == 3:
        if psum <= v:
            return ssum
        else:
            return 0
    if i > n or psum > v:
        return 0
    if (n-i + 1) < (3 -cnt):
        return 0
    ans1 = ra(n,v,w,ssum,psum,i+1,cnt)
    ans2 = ra(n,v,w,ssum+w[i-1],psum+i,i+1,cnt+1)
    return max(ans1,ans2)
n, v = map(int,input().split())
w = list(map(int,input().split()))
print(ra(n,v,w))
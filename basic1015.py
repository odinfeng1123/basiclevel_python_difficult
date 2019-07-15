def rr(l):
    l.sort(key = lambda x:x[0], reverse = False)
    l.sort(key = lambda x:x[1], reverse = True)
    l.sort(key = lambda x:x[3], reverse = True)
    return(l)
def judge(s,a,b,c,d,n):
    if s[1]>=n[2]: 
        if s[2]>=n[2]: a.append(s)
        elif s[2]>=n[1]: b.append(s)
    elif s[1]>=n[1] and s[2]>=n[1]:
        if s[1]>=s[2]: c.append(s)
        else: d.append(s)
n= list(map(int, input().split()))
a = []
b = []
c = []
d = []
for i in range(n[0]):
    s = list(map(int, input().split()))
    s.append(sum(s[1:]))
    judge(s,a,b,c,d,n)
output = rr(a) + rr(b) + rr(c) + rr(d)
print(str(len(output)))
for x in output:
    print(' '.join(list(map(str, x[:-1]))))
# 在多次提交下有可能能过第3测试点，但是第4、5测试点依然不能过

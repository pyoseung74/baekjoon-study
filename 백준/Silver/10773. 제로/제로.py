stk = []
pls = 0
K = int(input())
for _ in range(K):
    n = int(input())
    if n==0:
        stk.pop()
    else:
        stk.append(n)
for i in range(len(stk)):
    pls += stk.pop()

print(pls)
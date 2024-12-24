import sys

input = sys.stdin.readline

T = int(input().rstrip())
hap = []

for i in range(T):
    A,B = map(int,input().split())
    hap.append(A+B)


for j in range(T):
    print("Case #%d: %d" %(j+1 ,hap[j]))



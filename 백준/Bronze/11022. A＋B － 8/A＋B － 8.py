import sys

input = sys.stdin.readline

T = int(input().rstrip())
hap = []
printGO = []

for i in range(T):
    A,B = map(int,input().split())
    hap.append(A+B)
    printGO.append("Case #%d: %d + %d = %d" %(i+1 ,A,B,hap[i]))

for j in range(T):
    print(printGO[j])



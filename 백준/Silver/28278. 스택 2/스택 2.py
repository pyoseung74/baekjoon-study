import sys

input = sys.stdin.readline
stk = []    
N = int(input().rstrip())

for _ in range(N):
    command = input().split()

    if command[0] == '1':  # 1 X: 정수 X를 스택에 넣는다.
        x = int(command[1])
        stk.append(x)
    elif command[0] == '2':  # 2: 스택에서 맨 위의 정수를 제거하고 출력
        if not stk:
            print("-1")
        else:
            print(stk.pop())
    elif command[0] == '3':  # 3: 스택에 들어있는 정수의 개수를 출력
        print(len(stk))
    elif command[0] == '4':  # 4: 스택이 비어있으면 1, 아니면 0 출력
        if not stk:
            print("1")
        else:
            print("0")
    elif command[0] == '5':  # 5: 스택의 맨 위 값을 출력
        if not stk:
            print("-1")
        else:
            print(stk[-1])

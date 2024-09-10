import sys

input = sys.stdin.readline

dic = {')': '('}

T = int(input().rstrip())  # 테스트 케이스 수 입력
results = []  # 각 테스트 케이스의 결과를 저장할 리스트

for i in range(T):
    VPS = []  # 스택 초기화
    line = input().rstrip()  # 괄호 문자열 입력
    ans = "YES"  # 초기값을 "YES"로 설정

    for char in line:
        if char == '(':  # 여는 괄호면 스택에 추가
            VPS.append(char)
        else:
            if VPS:  # 닫는 괄호일 때 스택에 값이 있으면
                chk = VPS.pop()
                if dic[char] != chk:  # 매칭이 안 되면 "NO"
                    ans = "NO"
                    break
            else:  # 스택이 비어 있는데 닫는 괄호가 나왔을 때
                ans = "NO"
                break
    
    if VPS:  # 다 끝나고 스택에 값이 남아있으면 "NO"
        ans = "NO"
    
    results.append(ans)  # 결과를 리스트에 저장

# 저장된 결과를 출력
for result in results:
    print(result)

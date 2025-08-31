import sys
from collections import deque

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    # 입력 받은 문자열의 양쪽 공백 제거
    instruction = input().strip()

    # split()을 사용해 명령어를 분리
    parts = instruction.split()
    command = parts[0]

    if command == 'push':
        number = int(parts[1])
        queue.append(number)
    elif command == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
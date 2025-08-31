import sys

def check_match(PS):
    stack = []
    matching_dict = {
        ')': '('
    }
    for char in PS:
        if char in matching_dict.values():
            stack.append(char)
        elif char in matching_dict.keys():
            if not stack or stack[-1] != matching_dict[char]:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

T = int(input())
for tc in range(1, T+1):
    PS = sys.stdin.readline()
    result = check_match(PS)
    print(result)

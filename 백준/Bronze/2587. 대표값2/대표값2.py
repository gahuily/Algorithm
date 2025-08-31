import sys

sum = 0
number_list = []
for i in range(5):
    number = int(sys.stdin.readline())
    number_list.append(number)
    sum += number_list[i]

number_list.sort()

print(round(sum/5))
print(number_list[2])

first = 0
cur = 0
second = 0
third = 0

with open('input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    if line != '':
        cur += int(line)
    
    if line == '' or line == lines[-1]:
        if cur > first:
            third = second
            second = first
            first = cur
        elif cur > second:
            third = second
            second = cur
        elif cur > third:
            third = cur

        cur = 0

print(first)
print(second)
print(third)
print(first + second + third)
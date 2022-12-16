priority ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
score = 0

with open("Day3/input.txt") as f: 
    lines = f.readlines()

x = 0
while x < len(lines):
    c1 = lines[x].strip()
    c2 = lines[x+1].strip()
    c3 = lines[x+2].strip()
    score += priority.find(str(set(c1)&set(c2)&set(c3)).replace('{','').replace('}','').replace("'",'')) + 1
    x+=3




print(f'Part 1: {score}')

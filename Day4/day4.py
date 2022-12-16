with open("Day4/input.txt") as f: 
    lines = f.readlines()

score = 0
for line in lines:
    l = line.strip().split(",")
    e1 = l[0].split("-")
    e2 = l[1].split("-")
    e1low = int(e1[0])
    e1high = int(e1[1])
    e2low = int(e2[0])
    e2high = int(e2[1])


    if e1low >= e2low and e1low <= e2high: score += 1
            
    elif e2low >= e1low and e2low <= e1high: score += 1

print(f'Part 1: {score}')
with open("Day6/input.txt") as f: 
    lines = f.readlines()

for line in lines:
    line = line.strip()
    y=0
    z=14
    for x in line:
        if len(set(line[y:z])) == 14:
            print(z)
            break
        y+=1
        z+=1
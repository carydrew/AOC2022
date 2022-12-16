with open("Day5/input.txt") as f: 
    lines = f.readlines()


chart = lines[0:10] # chart
moves = lines[10:]  # moves from remainder of the input
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []
r8 = []
r9 = []

# make this into sideways chart left is bottomr, right is top.
for x in chart:
    z = -1
    for i in x:
        z+=1
        if i == ' ' or i == "[" or i == "]" or i == "\n": continue
        elif z == 1: r1.insert(0,i)
        elif z == 5: r2.insert(0,i)
        elif z == 9: r3.insert(0,i)
        elif z == 13: r4.insert(0,i)
        elif z == 17: r5.insert(0,i)
        elif z == 21: r6.insert(0,i)
        elif z == 25: r7.insert(0,i)
        elif z == 29: r8.insert(0,i)
        elif z == 33: r9.insert(0,i)
        else:
            print("You fucked up.")
print('Starting chart')
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)
print(r7)
print(r8)
print(r9)

for line in moves:
    x = line.strip().split(" ")
    move = int(x[1])
    f = int(x[3])
    t = int(x[5])

    i = 0
    while i<move:
        if f == 1: j = r1.pop()
        elif f == 2: j = r2.pop()
        elif f == 3: j = r3.pop()
        elif f == 4: j = r4.pop()
        elif f == 5: j = r5.pop()
        elif f == 6: j = r6.pop()
        elif f == 7: j = r7.pop()
        elif f == 8: j = r8.pop()
        elif f == 9: j = r9.pop()
        else:
            print("You fucked up.")
            break
        len(r1)
        if t == 1: r1.insert(len(r1)-i,j)
        elif t == 2: r2.insert(len(r2)-i,j)
        elif t == 3: r3.insert(len(r3)-i,j)
        elif t == 4: r4.insert(len(r4)-i,j)
        elif t == 5: r5.insert(len(r5)-i,j)
        elif t == 6: r6.insert(len(r6)-i,j)
        elif t == 7: r7.insert(len(r7)-i,j)
        elif t == 8: r8.insert(len(r8)-i,j)
        elif t == 9: r9.insert(len(r9)-i,j)
        else:
            print("You fucked up.")
            break
        i+=1

print('\nEnding chart')
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)
print(r7)
print(r8)
print(r9)

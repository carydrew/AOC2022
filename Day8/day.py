

def check_top(char, lines, row, col):
    r = 0
    while r < row:
        j = int(lines[r][col])
        if j >= char:
            return True
        r += 1
    return False

def check_bottom(char, lines, row, col):
    r = len(lines)-1
    while r > row:
        j = int(lines[r][col])
        if j >= char:
            return True
        r -= 1
    return False

def check_left(char, line, col):
    for l in line[:col]:
        if int(l) >= char:
            return True
    return False

def check_right(char, line, col):
    for l in line[1+col:]:
        if int(l) >= char:
            return True
    return False

def get_score(char, lines, row, col):
    print('Looking at {} at row {} and col {}'.format(char, row, col))

    # Top score 
    r = row - 1
    while r > 0:
        j = int(lines[r][col])
        if j >= char:
            break
        r-=1
    
    ts = row - r
    if ts == 0: ts = 1
    print(f"ts: {ts}")

    # Bottom score
    r = row + 1
    while r < len(lines) -1:
        j = int(lines[r][col])
        if j >= char:
            break
        r+=1    
    bs = r - row
    print(f"bs: {bs}")

    # Left score
    r = col-1
    while r > 0:
        l = lines[row][r]
        if int(l) >= char:
            break
        else:
            r-=1
    ls = col-r
    print(f"ls: {ls}")

    # Right score
    r = col
    for l in lines[row][1+col:]:
        r+=1
        if int(l) >= char:
            break
    rs = r - col

    print(f"rs: {rs}")

    score = ts * bs * ls * rs
    print(f"score: {score}\n")
    return score


def main():
    with open("Day8/input2.txt") as f:
        lines = f.readlines()
    
    lines = [i.strip() for i in lines]
    visable = len(lines) + len(lines[0]) - 2 + len(lines) + len(lines[0]) - 2
    #visable = 0
    not_visable = 0
    scenic = []
    sk = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            char = int(lines[row][col])
            if row == 0 or row == len(lines)-1 or col == 0 or col == len(lines[0])-1: # if on the edge
                sk +=1
                continue
            elif not check_bottom(char, lines, row, col) or not check_top(char, lines, row, col) or not check_left(char, lines[row], col) or not check_right(char, lines[row], col):
                visable += 1
                score = get_score(char,lines,row,col)
                scenic.append(score)
            else:
                not_visable += 1
            col += 1
        row += 1
    scenic.sort()
    #print(f"visable: {visable}")
    #print(f"not_visable: {not_visable}")
    #print(f"total counted: {visable + not_visable}")
    #print("Total should be 99x99 = 9801")
    #print(f"\nHighest Scenic: {scenic[-1]}")

    print(f"Part 1: {visable}")
    print(f"Part 2: {scenic[-1]}")
    #print(f"Part 2 Length: {len(scenic)+sk}")

if __name__ == "__main__":
    main()
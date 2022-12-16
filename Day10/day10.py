

def check_cycle(cycles:int,x:int) -> int:
    if cycles == 20:
        #print(f"20: {x*cycles}")
        return x*cycles
    else:
        c = cycles - 20
        if c % 40 == 0:
            print(f"{cycles}: {x} * {cycles} = {x*cycles}")
            return x*cycles
        else:
            return 0

def p2_check_cycle(cycles:int,x:int, p2:list[dict]) -> list[dict]:
    r = cycles//40
    c = cycles%40
    if c == x-1 or c == x or c == x+1:
        if len(p2)-1 == r:
            p2[r][c] = "#"
        else:
            p2.append({c:"#"})
    return p2

def do_cycle(cycles:int,x:int,p2:list[dict],sig_strength:int,num:int) -> tuple[int,int,list[dict],int]:
    cycle_count = 0
    while cycle_count < num:
        cycle_count += 1
        sig_strength += check_cycle(cycles,x)
        p2 = p2_check_cycle(cycles,x,p2)
        cycles += 1
    return cycles,x,p2,sig_strength

def main(lines:list[str]) -> None:

    # Part 1
    x = 1
    cycles = 0
    p2 = [{0:"#"}]
    sig_strength = 0
    for line in lines:
        part = line.split(" ")
        if part[0] == "noop":
            cycles,x,p2,sig_strength = do_cycle(cycles,x,p2,sig_strength,1)
            continue
        if part[0] == "addx":
            cycles,x,p2,sig_strength = do_cycle(cycles,x,p2,sig_strength,2)
            x += int(part[1])
            continue

    print(f"Part 1: {sig_strength}")

    # Part 2
    print("Part 2: \n")
    for i in p2:
        for j in range(0, 39):
            if i.get(j) == "#":
                print("O", end="")
            else:
                print(" ", end="")
        print("")




if __name__ == "__main__":
    with open("Day10/input.txt", "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    main(lines)
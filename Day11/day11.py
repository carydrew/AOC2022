

def main(lines):

    # Part 1

    # Find number of monkeys 
    monkeys = {}
    for line in lines:
        if line.lower().startswith("monkey"):
            monkeys[line.split(":")[0].strip()] = []
            name = line.split(":")[0].strip()
        elif line == "":
            continue
        else:
            monkeys.get(name).append(line.strip())

    # For each monkey seperate what they do
    for key in monkeys:
        items = monkeys.get(key)[0].split(":")[-1].strip().split(",")
        items = [int(item.strip()) for item in items]
        monkeys.get(key)[0] = items
        monkeys.get(key).append(0)
    j = 0
    while j < 10000: # change to 20 for part 1, part 2 = 10,000
        for key in monkeys:
            #Sprint(f"{key}: {monkeys.get(key)}")
            items = monkeys.get(key)[0]
            #print(f"{key}: {items}")
            test = int(monkeys.get(key)[2].split(" ")[-1].strip())
            t = monkeys.get(key)[3].split(" to ")[-1].strip().capitalize()
            f = monkeys.get(key)[4].split(" to ")[-1].strip().capitalize()
            operation = monkeys.get(key)[1]
            # each monkey messing with item
            while len(items) > 0:
                # inspection increase 
                item = monkeys.get(key)[0].pop(0)
                old = int(item)
                if "*" in operation:
                    if operation.count('old') > 1: item = old * old
                    else: item = old  * int(operation.split(" ")[-1].strip())
                elif "+" in operation:
                    if operation.count('old') > 1: item = old + old
                    else: item = old  + int(operation.split(" ")[-1].strip())
                else:
                    print("missed an operation")
                
                # End of inspection decrease
                # Uncomment for Part 1
                #item = item//3 

                item = item%(13*3*19*17*7*5*11*2)
                #item = item%(17*19*13*23)  # this is the test example for part2 

                # The test to throw to different monkey
                if int(item)%test == 0: 
                    monkeys.get(t)[0].append(item)
                else:
                    monkeys.get(f)[0].append(item)
                # Inspection increase
                monkeys.get(key)[-1] += 1
        j += 1




    # Get the score 
    score = []
    for key in monkeys:
        #print(f"{key}: {monkeys.get(key)[0]}")
        score.append(monkeys.get(key)[-1])

    #print(score)
    score.sort(reverse=True)
    print(f"Part 1: {score[0]*score[1]}")
    


if __name__ == "__main__":
    with open("Day11\input.txt", "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    main(lines)

    # 2713310158
    # 2633280540

    # 17245836796 - low
    # 17408399184
    # 18888105852 - high
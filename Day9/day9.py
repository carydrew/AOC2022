from math import dist
import time
import os
class Head():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = "0,0"
    
    def move(self, direction, distance):
        if direction == "R":
            self.x += distance
        elif direction == "L":
            self.x -= distance
        elif direction == "U":
            self.y += distance
        elif direction == "D":
            self.y -= distance
        else:
            print("Can't do that Watson")
        self.position = f"{self.x},{self.y}"
    
    def get_location(self):
        return self.x, self.y

class Body():
    def __init__(self):
        self.x = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        self.y = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        self.position = {1:"0,0",2:"0,0",3:"0,0",4:"0,0",5:"0,0",6:"0,0",7:"0,0",8:"0,0"}

    def move(self, location_x: int, location_y: int, part: int):
        # check diagonal   
        if part > 1: 
            location_x = self.x.get(part-1)
            location_y = self.y.get(part-1)
        if (dist([location_x], [self.x.get(part)]) >= 1 and dist([location_y], [self.y.get(part)]) > 1) or (dist([location_x], [self.x.get(part)]) > 1 and dist([location_y], [self.y.get(part)]) >= 1):
            
            if location_x - self.x.get(part) >= 1:
                self.x[part] += 1
            elif location_x - self.x.get(part) <= -1:
                self.x[part] -= 1
            if location_y - self.y.get(part) >= 1:
                self.y[part] += 1
            elif location_y - self.y.get(part) <= -1:
                self.y[part] -= 1

        # check vertical
        elif dist([location_y],[self.y.get(part)]) > 1:
            if location_y > self.y.get(part):
                self.y[part] += 1
            else:
                self.y[part] -= 1

        # check horizontal
        elif dist([location_x],[self.x.get(part)]) > 1:
            if location_x > self.x.get(part):
                self.x[part] += 1
            else:
                self.x[part] -= 1

        self.position[part] = f"{self.x.get(part)},{self.y.get(part)}"

    def get_end(self):
        return self.x.get(8), self.y.get(8)
    
    def get_front(self):
        return self.x.get(1), self.y.get(1)

    
class Tail():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = ["0,0"]
        self.position = "0,0"

    def move(self, location_x: int, location_y: int):
        # check diagonal
        if (dist([location_x], [self.x]) >= 1 and dist([location_y], [self.y]) > 1) or (dist([location_x], [self.x]) > 1 and dist([location_y], [self.y]) >= 1):
            #print("diagonal")
            if location_x - self.x >= 1:
                self.x += 1
            elif location_x - self.x <= -1:
                self.x -= 1
            if location_y - self.y >= 1:
                self.y += 1
            elif location_y - self.y <= -1:
                self.y -= 1

        # check vertical
        elif dist([location_y],[self.y]) > 1:
            if location_y > self.y:
                self.y += 1
            else:
                self.y -= 1

        # check horizontal
        elif dist([location_x],[self.x]) > 1:
            if location_x > self.x:
                self.x += 1
            else:
                self.x -= 1

        self.position = f"{self.x},{self.y}"

        if self.position not in self.visited:
            self.visited.append(self.position)

    def get_visited(self):
        #print(self.visited)
        confirmed = []
        for i in self.visited:
            if i not in confirmed:
                confirmed.append(i)
        #print(set(self.visited))
        #print(confirmed)
        return len(set(self.visited))

    def get_location(self): 
        return self.x, self.y
    
    def get_visits(self):
        return self.visited

def printer(head,tail):
    y = -20
    hx,hy = head.get_location()
    tx,ty = tail.get_location()
    sx,sy = 0,0
    print("=====================")
    while y < 20:
        x = -20
        while x < 20:
            if hx == tx and hy == ty and hx == x and hy == y:
                print("X", end="")
            elif hx == x and hy == y:
                print("H", end="")
            elif tx == x and ty == y:
                print("T", end="")
            elif sx == x and sy == y:
                print("S", end="")
            else:
                print("-", end="")
            x += 1
        print("")
        y += 1
    print("=====================")
    time.sleep(10)
    os.system("cls")

def print_vists(visted):
    y = -20
    v = visted
    print("=====================")
    while y < 20:
        x = -20
        while x < 20:
            if f"{x},{y}" in v:
                print("#", end="")
            else:
                print(".", end="")
            x += 1
        print("")
        y += 1
    print("=====================")


def main(lines: list):
    lines = [line.strip() for line in lines]
    head = Head()
    body = Body()
    tail = Tail()
    p2_tail = Tail()

    for line in lines:
        direction = line.split(" ")[0]
        distance = int(line.split(" ")[1])
        counter = 0
        while counter < distance:
            #printer(head, tail)  # uncomment to see the path
            head.move(direction, 1)
            # For part 1
            if dist(head.get_location(), tail.get_location()) > 1.5:
                tail.move(*head.get_location())
            # For part 2
            if dist(head.get_location(), body.get_front()) > 1.5:
                for i in range(1,9):
                    body.move(*head.get_location(), i)
            if dist(body.get_end(), p2_tail.get_location()) > 1.5:
                p2_tail.move(*body.get_end())
            counter += 1
            

    print(f"Part 1: The tail visited: {tail.get_visited()}")
    print("This is the tail's path: ")
    print(print_vists(tail.get_visits()))
    print(f"Part 2: The tail visited: {p2_tail.get_visited()}")
    print("This is the tail's path: ")
    print(print_vists(p2_tail.get_visits()))


if __name__ == "__main__":
    with open("Day9/input.txt") as f:
        lines = f.readlines()
    main(lines)

#5779 is right!! part 1 done.
#2331 is right!! part 2 done.





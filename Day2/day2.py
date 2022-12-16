def game(comp, user):
    rock_points = 1
    paper_points = 2
    scissors_points = 3

    # return same choice

    if comp == 'rock':
        if user == 'win':
            return paper_points
        elif user == 'lose':
            return scissors_points
    
    elif comp == 'paper':
        if user == 'lose':
            return rock_points
        elif user == 'win':
            return scissors_points
    
    elif comp == 'scissors':
        if user == 'win':
            return rock_points
        elif user == 'lose':
            return paper_points


def main():
    score = 0
    rock_points = 1
    paper_points = 2
    scissors_points = 3
    win = 6
    draw = 3
    lose = 0

    choice = {"A": "rock", "B": "paper", "C": "scissors"}
    p_outcome ={"X": "lose", "Y": "draw", "Z": "win"}

    with open("Day2/input.txt") as f:
        lines = f.readlines()
    
    for line in lines:
        line.split(" ")
        cchoice = choice.get(line[0])
        outcome = p_outcome.get(line[2])

        if outcome == "draw":
            score += draw
            uchoice = cchoice
            if uchoice == "rock": score += rock_points
            elif uchoice == "paper": score += paper_points
            elif uchoice == "scissors": score += scissors_points
        elif outcome == "win":
            score += win
            score += game(cchoice, outcome)
        elif outcome == "lose":
            score += lose
            score += game(cchoice, outcome)

    print(score)

if __name__ == "__main__":
    main()
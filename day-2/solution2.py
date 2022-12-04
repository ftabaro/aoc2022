import itertools

def predict_move(play):
    # X means you need to lose, 
    # Y means you need to end the round in a draw, 
    # and Z means you need to win
    move = None
    
    # p2 loses
    if play[1] == "X":
        # p1 plays rock 
        if play[0] == "A":
            # p2 plays scissor -> p2 loses
            move = "Z"
        # p1 plays paper 
        elif play[0] == "B":
            # p2 plays rock -> p2 loses
            move = "X"
        # p1 plays scissors
        elif play[0] == "C":
            # p2 plays paper -> p2 loses
            move = "Y"
    
    # tie
    elif play[1] == "Y":
        # p1 plays rock
        if play[0] == "A":
            # p2 plays rock
            move = "X"        
        # p1 plays paper
        elif play[0] == "B":
            # p2 plays paper
            move = "Y"
        # p1 plays scissors
        elif play[0] == "C":
            # p2 plays scissors
            move = "Z"

    # p2 wins
    elif play[1] == "Z":
        # p1 plays rock
        if play[0] == "A":
            # p2 plays paper -> p2 wins
            move = "Y"
        
        # p1 plays paper
        elif play[0] == "B":
            # p2 plays scissors -> p2 wins
            move = "Z"
        
        # p1 plays scissors
        elif play[0] == "C":
            # p2 plays rock -> p2 wins
            move = "X"

    return move


def main(path: str) -> int:

    # A for Rock, B for Paper, and C for Scissors
    p1_possible_outcomes = ["A", "B", "C"]

    # X for Rock, Y for Paper, and Z for Scissors
    p2_possible_outcomes = ["X", "Y", "Z"]

    # 1 for Rock, 2 for Paper, and 3 for Scissors
    scores = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    who_wins = {}
    for outcome in itertools.product(*[p1_possible_outcomes, p2_possible_outcomes ]):
        outcome = "".join(outcome)

        # p1 plays rock
        if outcome[0] == "A":
            
            # p2 plays rock
            if outcome[1] == "X":
                # rock vs rock
                who_wins[outcome] = "tie"
            
            # p2 plays paper
            elif outcome[1] == "Y":
                # rock vs paper -> paper wins
                who_wins[outcome] = "p2"
            
            # p2 plays scissors
            elif outcome[1] == "Z":
                # rock vs scissors -> rock wins
                who_wins[outcome] = "p1"
        
        # p1 plays paper
        elif outcome[0] == "B":

            # p2 plays rock
            if outcome[1] == "X":
                # paper vs rock -> paper
                who_wins[outcome] = "p1"
            
            # p2 plays paper
            elif outcome[1] == "Y":
                # paper vs paper -> tie
                who_wins[outcome] = "tie"
            
            # p2 plays scissors
            elif outcome[1] == "Z":
                # paper vs scissors -> scissors wins
                who_wins[outcome] = "p2"

        # p1 plays scissors
        elif outcome[0] == "C":

            # p2 plays rock
            if outcome[1] == "X":
                # scissors vs rock -> rock
                who_wins[outcome] = "p2"
            
            # p2 plays paper
            elif outcome[1] == "Y":
                # scissors vs paper -> scissors
                who_wins[outcome] = "p1"
            
            # p2 plays scissors
            elif outcome[1] == "Z":
                # scissors vs scissors -> scissors wins
                who_wins[outcome] = "tie"
            



    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    tie = 3 
    win = 6

    p1_score = 0    
    p2_score = 0
    with open(path) as fin:
        for i, line in enumerate(fin):
            play = line.strip().split(" ")
            play = "".join(play)
            
            p1_score += scores[play[0]]

            p2_move = predict_move(play)

            p2_score += scores[p2_move]

            winner = who_wins[play[0]+p2_move]

            if winner == "p1":            
                p1_score += win
            elif winner == "p2":
                p2_score += win
            elif winner == "tie":
                p1_score += tie
                p2_score += tie
            
            print(f"Round {i+1}: {play} - {p2_move} - {winner} match - p1={p1_score} - p2={p2_score}")
        

    print(p2_score)
    return p2_score

if __name__ == "__main__":
    import sys
    main(sys.argv[1])

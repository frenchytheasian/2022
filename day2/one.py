# Part one

guide = {'X': 1, 'Y': 2, 'Z': 3}
beats = {'Z': 'B', 'Y': 'A', 'X': 'C'}
ties = {'X': 'A', 'Y': 'B', 'Z': 'C'}
score = 0

with open('rps.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        
        moves = line.split(' ')
        my_move = moves[1]
        opp_move = moves[0]
        
        if beats[my_move] == opp_move:
            score += 6
        elif ties[my_move] == opp_move:
            score += 3
        else:
            score += 0
        
        score += guide[my_move]
        
        
print(score)

        
        
        
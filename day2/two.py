result = {'X': 0, 'Y': 3, 'Z': 6}
beats = {'A': 'B', 'B': 'C', 'C': 'A'}
loses = {'C': 'B', 'A': 'C', 'B': 'A'}
value = {'A': 1, 'B': 2, 'C': 3}

score = 0


def get_move(result: int, opp: int):
    if result == 'X': 
        return value[loses[opp]]
    elif result == 'Y':
        return value[opp]
    else :
        return value[beats[opp]]
    

with open('rps.txt', 'r') as f:
    for line in f.readlines():
        move = line.strip().split(' ')
        score += get_move(move[1], move[0])
        score += result[move[1]]
        print(move[0], move[1], score)
        
print(score)
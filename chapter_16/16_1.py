def top_down_score(score):
    def fb_score(score):
        if score < 0:
            return 0
        if score not in memo: 
            memo[score] = fb_score(score-2) + fb_score(score-3) + fb_score(score-7)
        return memo[score]
    memo = {0 : 1, 1:0}
    return fb_score(score)

def score_combo(score):
    table = [[0]*(score+1)]*3
    for i in range(score+1):
        if i % 2 == 0:
            table[0][i] = 1
    for i in range(score+1):
        if i >= 3:
            table[1][i] = table[0][i] + table[1][i-3]
        else:
            table[1][i] = table[0][i]

    for i in range(score+1):
        if i >= 7:
            table[2][i] = table[1][i] + table[2][i-7]
        else:
            table[2][i] = table[1][i]
    return(table[2][score])

if __name__ == '__main__':
    print('Ways to score 1 point', top_down_score(1))
    print('Ways to score 2 point', top_down_score(2))
    print('Ways to score 3 point', top_down_score(3))
    print('Ways to score 4 points',top_down_score(4))
    print('Ways to score 5 points',top_down_score(5))
    print('Ways to score 7 points',top_down_score(7))
        
    print('Combos to score 1 point', score_combo(1))
    print('Combos to score 2 point', score_combo(2))
    print('Combos to score 3 point', score_combo(3))
    print('Combos to score 5 point', score_combo(5))
    print('Combos to score 7 point', score_combo(7))
    print('Combos to score 9 point', score_combo(9))


"""
Find min distance
I.E. levinstein distance
"""

#to do: finish iterative version and memoize the other version
def get_distance(a, b):
    def LD(s, t):
        if s == "":
            return len(t)
        if t == "":
            return len(s)
        if s[-1] == t[-1]:
            cost = 0
        else:
            cost = 1
        delete = (s[:-1], t)
        if delete not in memo:
            memo[delete] = LD(*delete)
        insert = (s, t[:-1])
        if insert not in memo:
            memo[insert] = LD(*insert)
        replace = (s[:-1], t[:-1])
        if not replace in memo:
            memo[replace] = LD(*replace)
        return min(memo[delete]+1, memo[replace]+cost, 
            memo[insert]+1)
    memo = {}
    return LD(b,a)

def get_distance_iter(a,b):
    table = [[0 for x in range(len(b)+1)] for y in range(len(a)+1)]
    for i in range (0,(len(a)+1)):
        for j in range(0,(len(b)+1)):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            else:
                if a[i-1] == b[j-1]:
                    cost = 0
                else:
                    cost = 1
                table[i][j] = min(table[i-1][j-1]+cost, table[i][j-1]+1, table[i-1][j]+1)
    return table[i][j]

if __name__ == '__main__':
    print(get_distance('Saturday', 'Sundays'))
    print(get_distance_iter('Saturday','Sundays'))
    print(get_distance('Python','Pethein'))
    print(get_distance_iter('Python','Pethein'))
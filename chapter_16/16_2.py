"""
Find min distance
I.E. levinstein distance
"""

#to do: finish iterative version and memoize the other version

def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])
    return res

if __name__ == '__main__':
    print(LD("Python", "Peithen"))
    print(LD('Saturday', 'Sundays'))
"""
Towers of Hanoi problem

Write a prober which prints a sequence of operations that transfers n rights from one bed to another.  The only operation you can perform is taking a single ring from top of one peg and placing it on top of another peg.  You much never place a larger ring above a smaller ring

|   |   |
We can use 3 stacks to represent the pegs
Base case: one ring, move from peg A to peg B
Two rings:   move peg 1 to peg C
Move peg 2 to peg B 
Move peg 3 to peg B

3 pegs:

move ring 1 to peg B
move ring 2 to peg C
move ring 1 to peg C
move ring 3 to peg B
move ring 1 to peg A
move ring 2 to peg B
move ring 1 to peg B
"""

def compute_towers_of_hanoi(num_rings):
    def compute_towers_of_hanoi_helper(num, fro, to, use):
        if num > 0:
            compute_towers_of_hanoi_helper(num-1, fro, use, to)
            print('Moving Ring from Peg ', fro, ' to Peg ', to)
            ring = pegs[fro].pop()
            pegs[to].append(ring)
            compute_towers_of_hanoi_helper(num-1, use, to, fro)
    pegs = [[],[],[]]
    for ring in (reversed(range(num_rings))):
        pegs[0].append(ring+1)
    print(pegs)
    compute_towers_of_hanoi_helper(num_rings, 0, 1, 2)
    print(pegs)

# def compute_towers_of_hanoi(num_rings):
#     def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
#         if num_rings_to_move > 0:
#             compute_tower_hanoi_steps(
#                 num_rings_to_move - 1, from_peg, use_peg, to_peg)
#             pegs[to_peg].append(pegs[from_peg].pop())
#             print('Move from peg', from_peg, 'to peg', to_peg)
#             compute_tower_hanoi_steps(num_rings_to_move-1, use_peg, to_peg, from_peg)

#     NUM_PEGS = 3
#     pegs = [list(reversed(range(1, num_rings+1)))] + [[]
#             for _ in range(1, NUM_PEGS)]
#     compute_tower_hanoi_steps(num_rings, 0, 1, 2)
#     print(pegs)

if __name__ == '__main__':
    compute_towers_of_hanoi(1)
    print()
    compute_towers_of_hanoi(2)
    print()
    compute_towers_of_hanoi(3)

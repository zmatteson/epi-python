def n_queens(n):
    def solve_n_queens(row):
        if row == n:
            result.append(list(col_placement))
            return
        for col in range(n):
            if all(abs(c - col) not in (0, row -i )
                for i, c in enumerate(col_placement[:row])):
                    col_placement[row] = col
                    solve_n_queens(row+1)
    result, col_placement = [], [0] * n
    solve_n_queens(0)
    return result

if __name__ == '__main__':
    print(n_queens(6))
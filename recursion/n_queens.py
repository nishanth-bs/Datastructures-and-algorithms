def n_queens(n):
    res, col_placement = [],[0]*n
    
    def solve_n_queens(row):
        if n == row:
            res.append(list(col_placement))
            return
        for col in range(n):
            if all(
                abs(c - col) not in (0,row - i)
                for i,c in enumerate(col_placement[:row])):
                col_placement[row] = col
                solve_n_queens(row + 1)
    solve_n_queens(0)
    return res


print(n_queens(int(input('value of n (n*n)?'))))
            

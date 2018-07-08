#number of ways to traverse a 2D array to reach the bottom right entry
#paths must advance down or right

def numberOfWays(m,n):
    def noOfWaysToxy(x,y):
        if x == y == 0:
            return 1
        if noOfWays[x][y] == 0:
            waysTop = 0 if x == 0 else noOfWaysToxy( x-1, y)
            waysLeft = 0 if y == 0 else noOfWaysToxy(x,y-1)
            noOfWays[x][y] = waysTop + waysLeft
        return noOfWays[x][y]
    noOfWays = [[0] * m for _ in range(n)]
    return noOfWaysToxy(n-1, m-1)

print(numberOfWays(2,5))

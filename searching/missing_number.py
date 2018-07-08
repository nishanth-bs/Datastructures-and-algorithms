import math
#Given lowest-highest number's, all elements repeated m times,
#one element repeated n times

def find_missing(arr, lowest, highest, m, n):
    sums = m* (sum(range(lowest,highest)))
    diff = sums - sum(arr)
    return diff//(m-n)

lst = [5,5,5,3,4,6,7,8,9,2,3,4,6,7,8,9,2,3,4,6,7,8,9]
ans = find_missing(lst,2,10,3,2)
print(ans)

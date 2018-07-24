def no(a,b):
    n = 0
    for i in range(1, min(a,b) +1):
        if a%i ==0 and b%i == 0:
            n += 1
    return n

print(no(100000,12))
"""fh = open("ip00.txt",'a')

#for j in range(10):
#    for i in range(90000,90010):
#        if i != 90009:
#            fh.write(str(i))
#            fh.write(" ")
for i in range(5):
    fh.write(str(90009))
    fh.write(" ") 
fh.close()
"""

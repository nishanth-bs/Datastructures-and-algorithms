
#ip: nth number in the look and say sseries
def look_and_say(n):

    def nextNumber(no):
        count = 1
        result = []
        i = 0
        #print(no)
        while i < len(no):
            if i+1 < len(no) and no[i] == no[i+1]:
                count += 1
            else:
                result.append(str(count) + no[i])
                count = 1
            i += 1
        #print(result)
        return ''.join(result)
    no = '1'
    for _ in range(1,n):
        no = nextNumber(no)
    return no


print(look_and_say(8))

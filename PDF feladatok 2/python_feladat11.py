def derekszogu_e(a,b,c):
    numList = [a,b,c]
    max_value = max(numList)
    numList.remove(max_value)
    if numList[0]*numList[0] + numList[1]*numList[1] == max_value*max_value and max_value*max_value - numList[0]*numList[0] == numList[1]*numList[1] and max_value*max_value - numList[1]*numList[1] == numList[0]*numList[0]:
        return True
    else:
        return False 
print(derekszogu_e(int(input("a: ")), int(input("b: ")), int(input("c: "))))

valueDict = {'I': 1,
             'IV':4,
             'V': 5,
             'IX':9,
             'X': 10,
             'XL':40,
             'L': 50,
             'XC':90,
             'C': 100,
             'CD': 400,
             'D': 500,
             'CM': 900,
             'M': 1000}

def romanValue(test):
    sum = 0
    for i in range(len(test)-1,-1,-2):
        #print(test[i])
        p1 = test[i]
        p2 = test[i-1]
        print(p1,p2)
        if i == 0:
            sum = sum + valueDict[p1]
            print(sum)
            break
        if valueDict[p2] < valueDict[p1]:
            sum = valueDict[p1] - valueDict[p2] + sum
        else:
            sum = valueDict[p1] + valueDict[p2] + sum
        print(sum)

def romanMinimal():
    pass

def charCompare():
    pass

def main():
    test = 'MMMCDLXXXVII'
    test = list(test)
    #print(valueDict)
    romanValue(test)
    romanMinimal()
    charCompare()

main()



Y, M, D = map(int, input().split())

#윤년인지
def isTN(N):
    #4의 배수 근데 100의 배수는 아닌
    #400의 배수
    return (N % 4 == 0 and N % 100 != 0) or N % 400 == 0

#존재하는지
def isExist(Year, Month, Day):
    if isTN(Year):
            if (Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12) and 1 <= Day <= 31:
                return True
            elif (Month == 4 or Month == 6 or Month == 9 or Month == 11) and 1 <= Day <= 30:
                return True
            elif (Month == 2) and 1 <= Day <= 29:
                return True
    else:
            if (Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12) and 1 <= Day <= 31:
                return True
            elif (Month == 4 or Month == 6 or Month == 9 or Month == 11) and 1 <= Day <= 30:
                return True
            elif (Month == 2) and 1 <= Day <= 28:
                return True
    return False

#어떤계절인지
def whichSeason(Year, Month, Day):
    if isExist(Year, Month, Day):
        if Month == 12 or 1 <= Month <= 2:
            return 'Winter'
        if 3 <= Month <= 5:
            return 'Spring'
        if 6 <= Month <= 8:
            return 'Summer'
        if 9 <= Month <= 11:
            return 'Fall'
    return -1

print(whichSeason(Y,M,D))
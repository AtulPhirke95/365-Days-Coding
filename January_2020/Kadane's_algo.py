#kadane's algorithm:
def kadane(list_):
    stringtolast = 0
    stringsofar = 0
    flag_neg = all(x<0 for x in list_)
    if flag_neg == True:
        return max(list_)
    else:
        for _ in list_:
            stringtolast = stringtolast + _
            if stringtolast < 0:
                stringtolast = 0
            if stringsofar < stringtolast:
                stringsofar = stringtolast
        return stringsofar
T = int(input())   
while(T > 0):
    n = int(input())
    list_ = list(map(int, input().split()))
    print(kadane(list_))
    T -= 1
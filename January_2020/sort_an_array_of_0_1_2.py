#code
T = int(input())

while(T > 0):
    n = int(input())
    lis = list(map(int,input().split()))
    dict = {}
    string = ""
    
    for _ in lis:
        temp = dict.get(_,0)
        temp += 1
        dict[_] = temp
    
    string = "0 " * dict.get(0,0) + "1 " * dict.get(1,0) + "2 " * dict.get(2,0)

    print(string.strip())
            
    T -= 1

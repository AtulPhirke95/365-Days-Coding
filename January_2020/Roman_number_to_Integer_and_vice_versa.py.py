"""
    Roman number to integer
    Logic:  I can be placed before V (5) and X (10) to make 4 and 9. 
            X can be placed before L (50) and C (100) to make 40 and 90. 
            C can be placed before D (500) and M (1000) to make 400 and 900.
"""
dict = {"I":1,"V":5,"X":10,"L":50,"D":500,"C":100,"M":1000}

T = int(input())
while(T>0):
    roman = input()
    sum_=0
    i = 0
    while i < len(roman):
        if roman[i] == "I":
            if i != len(roman)-1 and roman[i+1] == "I" :
                sum_ += dict.get(roman[i])
            elif i != len(roman)-1 and roman[i+1] != "I":
                sum_ += dict.get(roman[i+1]) - dict.get(roman[i])
                break
            elif i == len(roman)-1:
                sum_ += dict.get(roman[i])
        elif roman[i] == "X":
            if i != len(roman)-1 and (roman[i+1] == "C" or roman[i+1] == "L"):
                sum_ += dict.get(roman[i+1]) - 10
                i = i+1
            else:
                sum_ += dict.get(roman[i])
        elif roman[i] == "C":
            if i != len(roman)-1 and (roman[i+1] == "M" or roman[i+1] == "D"):
                sum_ += dict.get(roman[i+1]) - 100
                i = i+1
            else:
                sum_ += dict.get(roman[i])
        else:
            sum_ += dict.get(roman[i])
        i+=1
    print(sum_)      
    T -= 1

"""
    Number to Roman
    Logic: Input 28 -> 10 , 18 -> 10 , 8 -> from dictionary value
"""
dict = {1: 'I', 2: "II",3:"III", 6: "VI", 7: "VII", 8: "VIII", 5: 'V', 10: 'X', 50: 'L', 500: 'D', 100: 'C', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'IL', 90: 'IC', 400: 'CD', 900: 'CM'}
lis = [1000,900,500,400,100,90,50,40,10,9,8,7,6,5,4,3,2,1]

def cal(n):
    for _ in lis:
        if n >= _:
            return _
n = 28
string = ""

while(n != 0):
    string += dict.get(cal(n))
    n = n - cal(n)
print(string)

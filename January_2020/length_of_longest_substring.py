"""
  Problem : Given a string, find the length of the longest substring without repeating characters. 
            For example, the longest substrings without repeating characters for “ABDEFGABEF” are “BDEFGA” and “DEFGAB”, with length 6.
  Input: 3
         geeksforgeeks
         qwertqwer
         qwertyuioijhghmnbvcdswwazxcv
  Output: 7 -> eksforg
          5 ->qwert
          10 -> ghmnbvcdsw
  Approach: Take lis and append the char until we get duplicate char. 
            If max <= count then update max with count and again update sublist starting from duplicate char to last.
            1)lis = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o']
              sub = oijhghmnbvcdswwazxcv
              max_ = 9
              count = 9
            2)lis = ['o', 'i', 'j', 'h', 'g']
              sub = ghmnbvcdswwazxcv
              max_ = 9
              count = 5
            3)lis = ['g', 'h', 'm', 'n', 'b', 'v', 'c', 'd', 's', 'w']
              sub = wazxcv
              max_ = 10
              count = 6
            if max_> count the print max_ else print count
"""
s1 = 'qwertyuioijhghmnbvcdswwazxcv'
lis = []
max_=0
count = 0
sub = s1
row = 0
i = 0
while(1):
    if not sub[i] in lis:
        lis.append(sub[i])
        count+=1
        i+=1
    else:
        if max_ <= count:
            max_ = count
        print(lis)
        del lis[:]
        row = s1.index(sub[i],row,row + count) + 1
        sub = s1[row:]
        print(sub)
        count = 0
        i=0
    if count == len(sub):
        if count > max_:
            print(count)
        else:
            print(max_)
        break

# level 1
a = [14, 27, 1, 4, 2, 50, 3, 1]
b = [2, 4, -4, 3, 1, 1, 14, 27, 50]
freq = dict()

for each in a:
    if each in freq:
        freq[each]+=1
    else:
        freq[each]=1

for each in b:
    if each in freq:
        if freq[each]==0:
            return each
        freq[each]-=1
    else:
        return each

for el in freq:
    if freq[el]==1: 
        return el

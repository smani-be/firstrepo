import re
fname = input("Enter file name:")
file = open(fname)

numlist = list()

for line in file:
    line = line.rstrip()
    sfind = re.findall('[0-9]+', line)
    if len(sfind) == 0: continue
    if len(sfind) > 1:
        for snum in sfind:
            num = float(snum)
            numlist.append(num)
    else:
        numlist.append(float(sfind[0]))

print('Sum:', int(sum(numlist)))    
        
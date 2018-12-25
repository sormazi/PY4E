fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    wds = line.split()
    #if len(wds) < 3 or not line.startswith('From'):
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])

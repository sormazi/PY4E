fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word_list = line.rstrip().split()
    # print(word_list)
    for element in word_list:
        if element in lst:
            continue
        else:
            lst.append(element)
lst.sort()
print(lst)

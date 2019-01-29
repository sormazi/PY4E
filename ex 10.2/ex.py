#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    word = line.split()
    if line.startswith('From '):
        count[word[1]] = count.get(word[1], 0) + 1
#largest = 0
#email = ''
#for k in count:
    #if count[k] > largest:
        #largest = count[k]
        #email = k
#print(email,largest)

bigcount = None
bigword = None
for k,v in count.items():
    if bigcount is None or v > bigcount:
        bigword = k
        bigcount = v

print(bigword,bigcount)

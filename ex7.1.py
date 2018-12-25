#Write a program that prompts for a file name, then opens that file and reads through the file
#print the contents of the file in upper case.
#Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt
f = input('Enter file name: ')
try:
    fh = open(f)
except:
    print("File does not exist. Program will be terminated.")
    quit()
for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())

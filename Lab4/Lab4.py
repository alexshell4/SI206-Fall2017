import re 

file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if re.search('From', line):
        print(line)
        numbers = re.findall('[0-9]+', line)
        print(numbers)
        name = re.findall('(\S+)@', line)
        print(name)
        

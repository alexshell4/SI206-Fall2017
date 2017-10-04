import re

txtfile = open('Actualdata.txt')
datafile = txtfile.read()
numfile = re.findall('[0-9]+', datafile)

sumfile = sum([int(x) for x in numfile])
print(sumfile)

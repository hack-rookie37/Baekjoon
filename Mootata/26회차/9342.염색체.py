import re

p = re.compile('^[A-F]?A+F+C+[A-F]?$')

for t in range(int(input())):
    chrom = input()
    if p.match(chrom) != None:
        print('Infected!')
    else:
        print('Good')
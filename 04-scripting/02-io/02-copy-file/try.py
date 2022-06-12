import sys

with open(sys.argv[1], 'r') as inf, open(sys.argv[2], 'w') as outf:
            for line in inf:
               outf.write(line)
    
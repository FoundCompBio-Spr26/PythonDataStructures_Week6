#! /usr/bin/python3

# Need the sys module for command-line arguments
import sys

# Expects the input file as 1st argument and output file as 2nd
print("infile: " + sys.argv[1])
print("outfile: " + sys.argv[2])

# Open input and output file streams
inFile = open(sys.argv[1],'r')
outFile = open(sys.argv[2],'w')

# Record sampling interval as 3rd command-line argument
interval = int(sys.argv[3])

# Use count variable to count lines as we go
count = 0

# Loop over lines in input file. Save every interval-th line in
# output file.
for line in inFile:
    if count % interval == 0:
        outFile.write(line)
    count = count + 1

# Close file streams
inFile.close()
outFile.close()

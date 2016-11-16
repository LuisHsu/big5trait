import sys
import os
import hashlib

# Check argv
if len(sys.argv) != 2:
	print "Usage: python dic2trait.py [Trait Dict]"
	sys.exit(1)

# Open file
traitFile = open(sys.argv[1], "r") # Trait file
hashFiles = []
os.mkdir("HashDict")
for i in range(0, 256):
	hashFiles.append(open("HashDict/%02x" % i, "w"))

# Read file
for line in traitFile:
	toks = line.split()
	word = toks.pop(0)
	traitFile = open(sys.argv[1], "a")
	hashFiles[int(hashlib.md5(word).hexdigest()[:2], 16)].write(line)
traitFile.close()
for f in hashFiles:
	f.close()

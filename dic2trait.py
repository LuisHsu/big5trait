import sys

# Check argv
if len(sys.argv) != 4:
	print "Usage: python dic2trait.py [Dict File] [Trait File] [Output File]"
	sys.exit(1)

# Open files
dicFile = open(sys.argv[1], "r") # Dictionary file
traitFile = open(sys.argv[2], "r") # Trait file
oupFile = open(sys.argv[3], "w") # Output file

# Read trait
traitDict = {} # The dictionary of traits
for line in traitFile:
	toks = line.split()
	trait = toks.pop(0)
	traitDict[trait] = toks

# Convert dict
for line in dicFile:
	toks = line.split()
	word = toks.pop(0).strip('*') # The word
	traits = [0.0, 0.0, 0.0, 0.0, 0.0]
	for category in toks:
		key = category
		if key in traitDict.keys():
			traitValues = traitDict[key]
			for i in range(0, 5):
				traits[i] += float(traitValues[i])
	oupFile.write(word + " %.2f %.2f %.2f %.2f %.2f" % (traits[0], traits[1], traits[2], traits[3], traits[4]) + '\n')

# Close files
dicFile.close()
oupFile.close()
traitFile.close()

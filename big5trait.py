import hashlib

def big5trait(wordList, traits, delta):
	ret = {
		"passed" : [],
		"failed" : []
	}
	for word in wordList:
		isfail = 1
		hashFile = open("HashDict/%s" % hashlib.md5(word).hexdigest()[:2], "r")
		for line in hashFile:
			toks = line.split()
			if(toks.pop(0) == word):
				for i in range(0, 5):
					if(abs(float(toks[i]) - traits[i]) <= delta):
						isfail = 0
						break
		if(isfail):
			ret["failed"].append(word)
		else:
			ret["passed"].append(word)
	return ret
						
						

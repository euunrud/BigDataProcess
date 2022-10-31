import sys

genres = dict()
with open(sys.argv[1], "rt") as fp:
	for line in fp:
		str1 = line.split("::")
		grlist = str1[2].split("|")
		for g in grlist:
			g = g.replace("\n", "")
			if g not in genres:
				genres[g] = 1
			else:
				genres[g] += 1

keys = genres.keys()
with open(sys.argv[2], "wt") as fp:
	for key in keys:
		fp.write(key + " " + str(genres[key]) + "\n")

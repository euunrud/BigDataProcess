import sys

gr1=["Comedy", "Fantasy", "Romance", "Animation", "Children's", "Adventure", "Drama", "Action", "Crime", "Thriller","Horror"]
gr2=[0,0,0,0,0,0,0,0,0,0,0]

with open(sys.argv[1], "rt") as fp:
	for line in fp:
		str1 = line.split("::")
		grlist = str1[2].split("|")
		for g in grlist:
#			print(g)
			for i in range(11):
				if gr1[i] in g:
					gr2[i] += 1
					break	
with open(sys.argv[2], "wt") as fp:
	for i in range(11):
		fp.write(gr1[i] + " " + str(gr2[i]) + "\n")

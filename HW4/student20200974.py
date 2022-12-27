#!/usr/bin/python3
import os
import operator
import sys
import numpy as np

trainingF = os.listdir(sys.argv[1])
list = os.listdir(sys.argv[2])

def readTest(fname):
	tList = []
	idx =0
	data = np.zeros((1, 1024))
	with open(fname) as f:
		for line in f.readlines():
			row = list(line)
			for i in row:
				if (i != '\n'):
					tList.append(float(i))
	data[idx, :] = tList
	return data

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
		sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

group, labels = fileToMat(sys.argv[1])

def fileToMat(folder):
	Label = []
	idx = 0
	leng = len(trainingF)
	data = np.zeros((leng, 1024))
		for i in range(0, leng):
			f = open(folder+"/"+trainingF[i])
			tList = []
			for line in range f.readlines():
				row = list(line)
				for k in row:
					if (k != '\n'):
						tList.append(float(k))
			data[idx, :] = tList
			fileNum = trainingF[i].split("_")
			Label.append(int(fileNum[0]))
			idx += 1
	return data, Label

leng = len(list)
for i in range(1, 21):
	total = 0
	error = 0
	for j in range(leng):
		testD = readTest(sys.argv[2]+"/"+list[i])
		sp= int(list[i].split("_")[0])
		predict = classify0(testD, group, labels, i)
		total += 1
		if a != predict:
			error += 1
	rslt = int((error / total) * 100)

	print(rslt)

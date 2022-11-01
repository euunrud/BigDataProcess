import calendar
import sys

weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
sameweek = dict()
arr = [0 for i in range(10000)]
flag = 0
with open(sys.argv[1], "rt") as fp:
		for line in fp:
			info = line.split(",")
			d = info[1].split("/")
			day = calendar.weekday(int(d[2]), int(d[0]), int(d[1]))
			s1 = info[0] +weekday[day] 
			if s1 not in sameweek:
				sameweek[s1] = flag
				arr[flag] = int(info[2])
				arr[flag + 1] = int(info[3])
#				print("f" + str(flag) + s1 + str(arr[flag]))
				flag += 2
			else:
				f = sameweek[s1]
				arr[f] += int(info[2])
#				print("--" + str(f) + s1 + str(arr[f]))
				arr[f + 1] += int(info[3])
with open(sys.argv[2], "wt") as fp2:
	keys = sameweek.keys()
	for key in keys:
		s1 = key[:6]
		s2 = key[6:]
		sv = sameweek[key]
		fp2.write(s1+","+s2+" "+str(arr[sv]) +","+ str(arr[sv+1])+ "\n")

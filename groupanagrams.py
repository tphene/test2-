a = ['ate','tea','and','dan','tae']
mp = {}

for i in a:
	t = sorted(i)
	print i
	print t 
	t = str(t)
	print t
	mp[i] = t
print mp
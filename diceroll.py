from random import randint


flag = True
while(flag == True):
	print "Do you want to rolls the dice?0 for yes else any key for no"
	ip = raw_input()
	if(isinstance(ip,int)):
		if(ip == 0):
			print(randint(1,6))
		else:
			break
	else:
			break

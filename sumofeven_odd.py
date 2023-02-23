n=int(input('enter a number:'))
i=sume=sumo=0
while(i <= n):
	if(i%2==0):
		sume=sume+i
		i=i+1
	elif(i%2!=0):
		sumo=sumo+i
		i=i+1
print('sum of even num:',sume)
print('sum of odd num:',sumo)
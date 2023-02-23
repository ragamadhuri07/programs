n= int(input('enter a digit:'))
sum=0
while(n!=0):
	r=n%10
	sum=sum+r
	n=n//10
print('sum of given digit:',sum)
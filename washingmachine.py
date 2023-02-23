n=int(input('enter the weight:'))
if n<2000:
	print('under weight to run machine')
elif n in range(2001:4001):
	print('machine takes 25 mins to compelete')
elif n in range(4001:6999):
	print('machines takes 45 mins to complete')
elif n>7000:
	print('OVERLOAD')
else:
	print('invalid input')
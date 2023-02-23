a=int(input('enter a value:'))
b=int(input('enter b value:'))
c=int(input('enter c value:'))
if a>b:
	if a>c:
		print('a is the largest')
if b>a:
	if b>c:
		print('b is the largest')
if c>a:
	if c>b:
		print('c is the largest')
else:
	print('all are equal')
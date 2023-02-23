dn=int(input('enter decimal value:'))
bn=i=0
while dn!=0:
	r=dn%2
	bn=bn+r*(10**i)
	dn=dn//2
	i=i+1
print(bn)
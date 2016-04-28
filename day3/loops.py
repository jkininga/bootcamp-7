a=[10,40,-9,45,60,89]



i=len(a)
# while i > 0:
# 	print a[i-1]
# 	i-=1

for x in range(len(a) -1, -1 , -1):
	print a[x]


b = [(2,4),(7,8),(4,5), (6,8,9)]

for m in b:
	i=len(m)
	if i > 2:
		print 'x: {}, y: {}, z: {}'.format(m[0], m[1], m[2])
	else:
		print 'x: {}, y: {}'.format(m[0], m[1])





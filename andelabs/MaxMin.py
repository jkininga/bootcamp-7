def find_max_min(a):
	x = min (a)
	y = max (a)
	
	if x == y:
	  return [len(a)]
	return [x, y]

print find_max_min([4,7,8,9])		
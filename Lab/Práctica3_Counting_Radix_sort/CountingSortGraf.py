contador = 0
def countingSort(A, maxVal):
	global contador 
	count = [0] * (maxVal + 1)
	for a in A:
		contador += 1
		count[int(a.id)] += 1
	i = 0
	for a in range(maxVal + 1):
		for c in range(count[a]):
			contador += 1
			A[i].id = a
			i += 1
	return contador




arr = []
for _ in range(9):
	arr.append(int(input()))

sum = sum(arr)
temp_a, temp_b =0, 0

for i in range(9):
	for j in range(i+1, 9):
		if sum - arr[i] - arr[j] == 100:
			temp_a, temp_b = arr[i], arr[j]
			break
arr.remove(temp_a)
arr.remove(temp_b)
arr.sort()

for k in range(len(arr)):
	print(arr[k])
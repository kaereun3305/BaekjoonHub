import sys
T = int(sys.stdin.readline())
arr=[]
sum_arr= 0
for _ in range(T):
  x = int(sys.stdin.readline())
  arr.append(x)
  sum_arr += x

arr.sort()

if sum_arr <0:
  print(0 - abs(sum_arr//T + (1 if (sum_arr/T - sum_arr//T)>=0.5 else 0)))
else:
  print(sum_arr//T + (1 if (sum_arr/T - sum_arr//T)>=0.5 else 0))
print(arr[T//2])

dict = {}
for i in arr:
  if i not in dict:
    dict[i] = 1
  else:
    dict[i] += 1
max_cnt = max(dict.values())
max_arr = sorted([j for j,k in dict.items() if k == max_cnt])
if len(max_arr)>1:
  print(max_arr[1])
else:
  print(max_arr[0])


print(arr[-1] - arr[0])
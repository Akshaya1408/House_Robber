arr = list(map(int,input().split()))
count = 0
for i in range(0,len(arr),2):
    count = count + arr[i]
print(count)

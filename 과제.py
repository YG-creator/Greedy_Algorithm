'''
N = int(input())
d_w = [list(map(int,input().split())) for _ in range(N)]
d_w.sort(key=lambda x:x[1],reverse = True)
sum = 0
day = 1
for i in range(N) :
    if day <= d_w[i][0] :
        sum += d_w[i][1]
        day += 1
print(sum)
'''
import sys
import heapq
n = int(sys.stdin.readline().rstrip("\n"))
nums = []
sums = [0]*(1000+1)
for i in range(n):
    day, value = map(int, sys.stdin.readline().rstrip("\n").split())
    nums.append([-value,day,value])
heapq.heapify(nums)
while nums:
    temp = heapq.heappop(nums)
    for i in range(temp[1],0,-1):
        if(sums[i]==0):
            sums[i]=temp[2]
            break

print(sum(sums))

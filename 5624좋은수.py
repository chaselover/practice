import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
dp = [0]*400003
tmp = 200001

answer = 0
for i in range(N):
    for j in range(i):
        if dp[arr[i] - arr[j]+tmp]==1:
            answer+=1
            break
    for k in range(i+1):
        dp[arr[i]+arr[k]+tmp] = 1
    
print(answer)
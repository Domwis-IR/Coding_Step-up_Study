n, k = map(int, input().split())

coin_list = []
for _ in range(n):
    i = int(input())
    coin_list.append(i)

INF = float('inf')
dp = [INF] * (k + 1)
dp[0] = 0

for coin in coin_list:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != 0 else -1) 
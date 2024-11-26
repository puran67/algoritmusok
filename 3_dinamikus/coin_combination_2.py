MOD = 10**9 + 7

def count_ways(n, sum, coins):
    dp = [0] * (sum + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, sum + 1):
            dp[i] = (dp[i] + dp[i - coin]) % MOD

    return dp[sum]

# Beolvasás
n, x = map(int, input().split())
coins = list(map(int, input().split()))

# Eredmény kiírása
print(count_ways(n, x, coins))
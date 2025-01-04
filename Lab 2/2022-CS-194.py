
def fibonacci(n,storedValues={}):
    if n==0:
        return 0
    if n==1:
        return 1
    
    if n in storedValues:
        return storedValues[n]
    
    storedValues[n]=fibonacci(n-1,storedValues)+fibonacci(n-2,storedValues)
    return storedValues[n]

n=10
print(f"Fibonacci({n})={fibonacci(n)}")


def coin_change(coins, target):
    coins.sort(reverse=True) 
    count = 0  
    for coin in coins:
        while target >= coin:
            target -= coin  
            count += 1 
 
    return count if target == 0 else -1

coins = [1, 2, 5]
target = 100
result = coin_change(coins, target)
print(f"Minimum number of coins to make {target}: {result}")


def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]: 
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
  
    return dp[m][n]

X = "Ifra"
Y = "ifazalifra"
result = longest_common_subsequence(X, Y)
print(f"Length of the longest common subsequence: {result}")


def count_ways_to_climb(n):
    if n == 0:
        return 1 
    elif n == 1:
        return 1  
    dp = [0] * (n + 1)
    dp[0] = 1  
    dp[1] = 1 
    
  
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

n = 10
print(f" ways to climb {n} stairs: {count_ways_to_climb(n)}")



def knapsack(weights, values, capacity):
    n = len(weights) 
    
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
 
    for i in range(1, n + 1):  
        for w in range(capacity + 1): 
            if weights[i - 1] <= w:
               
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
     
    return dp[n][capacity]

weights = [1, 2, 3]
values = [10, 20, 30]
capacity = 5
print(f"Max value: {knapsack(weights, values, capacity)}")

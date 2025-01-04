 # Q1

def edit_distance_recursive(s1, s2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if s1[m - 1] == s2[n - 1]:
        return edit_distance_recursive(s1, s2, m - 1, n - 1)
    return 1 + min(edit_distance_recursive(s1, s2, m, n - 1),   
                   edit_distance_recursive(s1, s2, m - 1, n),   
                   edit_distance_recursive(s1, s2, m - 1, n - 1) 
                  )

s1 = "kitty"
s2 = "sitting"
print(edit_distance_recursive(s1, s2, len(s1), len(s2)))




def edit_distance_memo(s1, s2, m, n, memo):
    if m == 0:
        return n
    if n == 0:
        return m
    if memo[m][n] != -1:
        return memo[m][n]
    if s1[m - 1] == s2[n - 1]:
        memo[m][n] = edit_distance_memo(s1, s2, m - 1, n - 1, memo)
    else:
        memo[m][n] = 1 + min(edit_distance_memo(s1, s2, m, n - 1, memo),    
                             edit_distance_memo(s1, s2, m - 1, n, memo),    
                             edit_distance_memo(s1, s2, m - 1, n - 1, memo)
                             )
    return memo[m][n]

def edit_distance_memoization(s1, s2):
    m = len(s1)
    n = len(s2)
    memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    return edit_distance_memo(s1, s2, m, n, memo)

s1 = "kitten"
s2 = "sitting"
print(edit_distance_memoization(s1, s2))




def edit_distance_tabulation(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],    
                                   dp[i - 1][j],    
                                   dp[i - 1][j - 1] 
                                   )
    return dp[m][n]

s1 = "kitten"
s2 = "sitting"
print(edit_distance_tabulation(s1, s2))




def edit_distance_iterative(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[m][n]

s1 = "kitten"
s2 = "sitting"
print(edit_distance_iterative(s1, s2))


#Q2 

def balance_recursive(s, index, open_count, close_count):
    if index == len(s):
        return '(' * (close_count - open_count) + s + ')' * (open_count - close_count)
    
    if s[index] == '(':
        return balance_recursive(s, index + 1, open_count + 1, close_count)
    elif s[index] == ')':
        if open_count > close_count:
            return balance_recursive(s, index + 1, open_count, close_count + 1)
        else:
            return '(' + balance_recursive(s, index + 1, open_count + 1, close_count)
    else:
        return s[index] + balance_recursive(s, index + 1, open_count, close_count)

def balance_unbalanced_recursive(s):
    return balance_recursive(s, 0, 0, 0)

s = "(a+b(c)"
print(balance_unbalanced_recursive(s))



def balance_unbalanced_iterative(s):
    open_needed = 0
    close_needed = 0
    
    for char in s:
        if char == '(':
            close_needed += 1
        elif char == ')':
            if close_needed > 0:
                close_needed -= 1
            else:
                open_needed += 1

    return '(' * open_needed + s + ')' * close_needed

s = "(a+b(c)"
print(balance_unbalanced_iterative(s))


#Q3
def alignment_recursive(S, T, i, j, match_score, mismatch_penalty, gap_penalty):
    if i == 0:
        return j * gap_penalty
    if j == 0:
        return i * gap_penalty
    
    match_or_substitution = (match_score if S[i-1] == T[j-1] else mismatch_penalty) + alignment_recursive(S, T, i-1, j-1, match_score, mismatch_penalty, gap_penalty)
    gap_in_S = alignment_recursive(S, T, i-1, j, match_score, mismatch_penalty, gap_penalty) + gap_penalty
    gap_in_T = alignment_recursive(S, T, i, j-1, match_score, mismatch_penalty, gap_penalty) + gap_penalty
    
    return max(match_or_substitution, gap_in_S, gap_in_T)

S = "AGGTAB"
T = "GXTXAYB"
match_score = 2
mismatch_penalty = -1
gap_penalty = -2
print(alignment_recursive(S, T, len(S), len(T), match_score, mismatch_penalty, gap_penalty))





def alignment_tabulation(S, T, match_score, mismatch_penalty, gap_penalty):
    m = len(S)
    n = len(T)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i * gap_penalty
    for j in range(n + 1):
        dp[0][j] = j * gap_penalty
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match_or_substitution = dp[i-1][j-1] + (match_score if S[i-1] == T[j-1] else mismatch_penalty)
            gap_in_S = dp[i-1][j] + gap_penalty
            gap_in_T = dp[i][j-1] + gap_penalty
            dp[i][j] = max(match_or_substitution, gap_in_S, gap_in_T)
    
    return dp[m][n]

S = "AGGTAB"
T = "GXTXAYB"
match_score = 2
mismatch_penalty = -1
gap_penalty = -2
print(alignment_tabulation(S, T, match_score, mismatch_penalty, gap_penalty))





def alignment_iterative(S, T, match_score, mismatch_penalty, gap_penalty):
    m = len(S)
    n = len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i * gap_penalty
    for j in range(n + 1):
        dp[0][j] = j * gap_penalty
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                score = match_score
            else:
                score = mismatch_penalty
            dp[i][j] = max(dp[i - 1][j - 1] + score, dp[i - 1][j] + gap_penalty, dp[i][j - 1] + gap_penalty)
    
    return dp[m][n]

S = "AGGTAB"
T = "GXTXAYB"
match_score = 2
mismatch_penalty = -1
gap_penalty = -2
print(alignment_iterative(S, T, match_score, mismatch_penalty, gap_penalty))



#Q4

def min_coins_recursive(coins, N):
    if N == 0:
        return 0
    result = float('inf')
    
    for coin in coins:
        if N - coin >= 0:
            sub_res = min_coins_recursive(coins, N - coin)
            if sub_res != float('inf'):
                result = min(result, sub_res + 1)
    
    return result

coins = [1, 2, 5]
N = 11
print(min_coins_recursive(coins, N))




def min_coins_memo(coins, N, memo):
    if N == 0:
        return 0
    if memo[N] != -1:
        return memo[N]
    
    result = float('inf')
    
    for coin in coins:
        if N - coin >= 0:
            sub_res = min_coins_memo(coins, N - coin, memo)
            if sub_res != float('inf'):
                result = min(result, sub_res + 1)
    
    memo[N] = result
    return memo[N]

def min_coins_memoization(coins, N):
    memo = [-1] * (N + 1)
    return min_coins_memo(coins, N, memo)

coins = [1, 2, 5]
N = 11
print(min_coins_memoization(coins, N))




def min_coins_tabulation(coins, N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[N] if dp[N] != float('inf') else -1

coins = [1, 2, 5]
N = 11
print(min_coins_tabulation(coins, N))




def min_coins_iterative(coins, N):
    dp = [0] + [float('inf')] * N
    
    for i in range(1, N + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[N] if dp[N] != float('inf') else -1

coins = [1, 2, 5]
N = 11
print(min_coins_iterative(coins, N))

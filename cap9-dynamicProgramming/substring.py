def longest_common_substring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_pos = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i
            else:
                dp[i][j] = 0
                
    # Recupa a substring
    lcs = s1[end_pos - max_len:end_pos]
    return max_len, lcs

s1 = "blue"
s2 = "clues"
length, substring = longest_common_substring(s1, s2)

print(f"Maior Substring Comum: '{substring}', Tamanho: {length}")
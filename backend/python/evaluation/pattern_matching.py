def isMatch(text, pattern):
    m, n = len(text), len(pattern)


    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True

    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]


    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == '.' or pattern[j - 1] == text[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if text[i - 1] == pattern[j - 2] or pattern[j - 2] == '.' else False)

    return dp[m][n]

example_one = {"text": "abbbc", "pattern": "ab*c"}
example_two = {"text": "abcdefg", "pattern": "a.c.*.*gg*"}

print(int(isMatch(example_one["text"], example_one["pattern"])))
print(int(isMatch(example_two["text"], example_two["pattern"])))  

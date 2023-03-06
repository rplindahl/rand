import math

def binomial_option_price(S, K, r, T, sigma, n, is_call):
    dt = T / n
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    p = (math.exp(r * dt) - d) / (u - d)

    # Create a 2D array to store the option prices at each node of the tree
    option_prices = [[0] * (i + 1) for i in range(n + 1)]

    # Fill in the option prices for the final nodes of the tree
    for i in range(n + 1):
        if is_call:
            option_prices[n][i] = max(0, S * (u ** i) * (d ** (n - i)) - K)
        else:
            option_prices[n][i] = max(0, K - S * (u ** i) * (d ** (n - i)))
   # print(option_prices)   #test

    # Work backwards through the tree, filling in the option prices at each node
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            option_prices[i][j] = math.exp(-r * dt) * (
                        p * option_prices[i + 1][j + 1] + (1 - p) * option_prices[i + 1][j])

    # Return the option price at the root node of the tree
    #print(option_prices)    #test
    return option_prices[0][0]

print(binomial_option_price(100, 90, 0.03, 30, 0.30, 10, True))


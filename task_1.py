import timeit

mysetup="""
from __main__ import find_coins_greedy
from __main__ import find_dynamic_coins
from __main__ import coin_denominations_2
from __main__ import coin_denominations_1
from __main__ import amount
"""

def find_coins_greedy(amount, coin_denominations):
    result = {}
    for coin in coin_denominations:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    
    if amount > 0:
        print("Залишок, який неможливо видати монетами: ", amount)
    return result


def find_dynamic_coins(amount, coin_denominations):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_count = [{} for _ in range(amount + 1)]
    
    for coin in coin_denominations:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin_count[i - coin].copy()
                if coin in coin_count[i]:
                    coin_count[i][coin] += 1
                else:
                    coin_count[i][coin] = 1
    
    if dp[amount] == float('inf'):
        return "Неможливо видати задану суму."
    
    return coin_count[amount]

coin_denominations_1 = [1, 5, 10, 25, 50]
coin_denominations_2 = [50, 25, 10, 5, 1]
amount = 7395

print(f"result by greedy_method = {find_coins_greedy(amount,coin_denominations_2)}")
print(f"result by dynamic_method = {find_dynamic_coins(amount, coin_denominations_1)}")

time_greedy = timeit.timeit(stmt="find_coins_greedy(amount,coin_denominations_2)", setup=mysetup, number=5)
time_dynamic = timeit.timeit(stmt="find_dynamic_coins(amount,coin_denominations_1)", setup=mysetup, number=5)

print(f"\nЧас виконання жадібного методу = {time_greedy:.08f}")
print(f"\nЧас виконання динамічного методу = {time_dynamic:.08f}")
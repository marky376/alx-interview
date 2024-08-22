#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount toatal when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_tx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_tx >= n:
            return -1
        if rem - sorted_coins[coin_tx] >= 0:
            rem -= sorted_coins[coin_tx]
            coins_count += 1
        else:
            coin_tx += 1
    return coins_count

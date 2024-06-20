def find_min_coins(sum):
    coins = [1, 2, 5, 10, 25, 50]
    min_coins_required = [0] + [float('inf')] * sum
    coin_used = [0] * (sum + 1)

    for i in range(1, sum + 1):
        for coin in coins:
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coin_used[i] = coin
    print(min_coins_required)
    print(coin_used)
    
    coins_count = {}
    current_sum = sum
    while current_sum > 0:
        coin = coin_used[current_sum]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_sum -= coin

    return coins_count


if __name__ == '__main__':
    coins_needed = find_min_coins(113)
    print(coins_needed)
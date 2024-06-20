def find_coins_greedy(sum):
    coins = [50, 25, 10, 5, 2, 1]
    coins_count = {}

    for coin in coins:
        count = sum // coin
        if count > 0:
            coins_count[coin] = count
        sum -= coin * count 

    return coins_count


if __name__ == '__main__':

    
    coins_needed_greedy = find_coins_greedy(113)
    print(coins_needed_greedy)
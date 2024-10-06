from crypto_data import get_coins, Coin
import time

def alert(symbol:str, bottom: float, top: float, coin_list: list[Coin]): 
    for coin in coin_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, '!!TRIGGERED!!')
            else:
                print(coin)

if __name__ == '__main__':
    coins: list[Coin] = get_coins()
    while True:
        time.sleep(3)
        alert('btc', bottom=59_000, top=60_000, coin_list=coins)
        alert('eth', bottom=59_000, top=60_000, coin_list=coins)
        alert('usdt', bottom=0.922222, top=0.98888, coin_list=coins)
                
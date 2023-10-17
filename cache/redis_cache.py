import io

import redis
import pandas as pd

if __name__ == "__main__":
    timeout = 60000
    redis_client = redis.StrictRedis(host="localhost", port=6379, socket_timeout=timeout)
    stock_price = pd.read_csv("D:/stock/data/latest/stock_price.csv", encoding="utf-8")
    print(type(stock_price))
    print(type(stock_price.to_csv()))
    redis_client.set("stock_price", stock_price.to_csv())
    str_stock_price = redis_client.get('stock_price')
    print(type(str_stock_price))
    #df = pd.read_csv(df)
    df = pd.read_csv(io.StringIO(str_stock_price.decode('utf-8')))
    print(df)
    print("completed!")


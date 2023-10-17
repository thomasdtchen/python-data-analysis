import io

import redis
import pandas as pd
import json
# when a = [x for x in range(10 ** 7)] is fine, 84.7 MB
# when a = [x for x in range(10 ** 8)] 943 MB
# Key的大小上限为512M。 建议key的大小不超过1KB，这样既节约存储空间，也利于Redis进行检索。 String类型的value值上限为512M
# as tried, when the str is 184 MB ([x for x in range((10 ** 7)*2)]) or 288MB ([x for x in range((10 ** 7)*3)]), it works fine
# so the root cause is redis only allow a 512MB string
#redis.exceptions.ConnectionError: Error 10054 while writing to socket. An existing connection was forcibly closed by the remote host.
if __name__ == "__main__":
    timeout = 6000
    redis_client = redis.StrictRedis(host="localhost", port=6379, decode_responses=True, socket_timeout=timeout)
    a = [x for x in range((10 ** 7)*3)]
    print(type(a))
    redis_client.set("large_object", json.dumps(a))
    #with open("large_object3.txt", "w", encoding="utf-8") as file:
    #    file.write(json.dumps(a))
    a = json.loads(redis_client.get("large_object"))
    print(a)
    print("completed!")


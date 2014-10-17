import redis
import sys

r = redis.Redis("localhost")

ps_obj=r.pubsub()
ps_obj.subscribe(sys.argv[1])

for item in ps_obj.listen():
    print item['data']


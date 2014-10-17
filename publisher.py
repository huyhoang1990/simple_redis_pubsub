import redis
import sys

r = redis.Redis("localhost")
r.publish(sys.argv[1],"["+sys.argv[2]+"] " + " ".join(sys.argv[3:]))


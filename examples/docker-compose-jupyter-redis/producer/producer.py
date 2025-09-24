import redis
import time

r = redis.Redis(host='redis', port=6379, db=0)

print("Producer is starting...")
while True:
    timestamp = time.time()
    message = f"Message sent at {timestamp}"
    print(f"Producer sending: '{message}'")
    r.set('latest_message', message)
    time.sleep(5)
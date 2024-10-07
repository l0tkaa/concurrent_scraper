import time
import random

class RateLimiter:
    def __init__(self, min_delay=1, max_delay=5):
        self.min_delay = min_delay
        self.max_delay = max_delay

    def wait(self):
        delay = random.uniform(self.min_delay, self.max_delay)
        print(f"Waiting for {delay:.2f} seconds before next request...")
        time.sleep(delay)

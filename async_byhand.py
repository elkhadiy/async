import time
from collections import deque
import heapq

class Scheduler:
    def __init__(self):
        self.ready = deque()
        self.sleeping = []
        self.sequence = 0  # avoid tie-breaking deadlines

    def call_soon(self, func):
        self.ready.append(func)

    def call_later(self, delay, func):
        self.sequence += 1
        deadline = time.time() + delay
        heapq.heappush(self.sleeping, (deadline, self.sequence, func))

    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                deadline, func = heapq.heappop(self.sleeping)
                delta = deadline - time.time()
                if delta > 0:
                    time.sleep(delta)
                self.ready.append(func)
            
            while self.ready:
                func = self.ready.popleft()
                func()


if __name__ == '__main__':

    sched = Scheduler()

    def countdown(n):
        if n > 0:
            print('Down', n)
            sched.call_later(4, lambda: countdown(n-1))

    def countup(stop, x=0):
        if x < stop:
            print('Up', x)
            sched.call_later(1, lambda: countup(stop, x=x+1))

    sched.call_soon(lambda: countdown(5))
    sched.call_soon(lambda: countup(20))

    sched.run()
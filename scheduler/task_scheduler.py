import time
from collections import deque


class TaskScheduler:

    def __init__(self):

        self.queue = deque()

        self.max_tasks = 5
        self.retry_limit = 2

    def add_task(self, goal):

        if len(self.queue) < self.max_tasks:

            self.queue.append({
                "goal": goal,
                "retries": 0
            })

    def next_task(self):

        if not self.queue:
            return None

        return self.queue.popleft()

    def retry_task(self, task):

        if task["retries"] < self.retry_limit:

            task["retries"] += 1
            self.queue.append(task)

    def wait_cycle(self):

        time.sleep(10)
import queue

task_queue = queue.Queue()

def add_task(task):
    task_queue.put(task)

def get_task():
    if not task_queue.empty():
        return task_queue.get()
    return None

def has_tasks():
    return not task_queue.empty()
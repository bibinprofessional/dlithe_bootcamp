from queue import Queue

class Task:

    def __init__(self):
        self.task_queue=Queue()

    def schedule_task(self,tasks):
        for task in tasks:
            self.task_queue.put(task)

    def do_task(self):
        if not self.task_queue.empty():
            current_task = self.task_queue.get()
            print(f"Processing task: {current_task}")


tasks = ["Task 1", "Task 2", "Task 3", "Task 4"]
t=Task()
t.schedule_task(tasks)
t.do_task()
t.schedule_task(['tad'])
t.do_task()
t.do_task()
t.do_task()
t.do_task()


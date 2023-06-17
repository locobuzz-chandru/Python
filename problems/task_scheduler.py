from bst import BinaryTree
from datetime import datetime
from collections import namedtuple


class Task:
    def __init__(self, task_id: int, description: str):
        self.id = task_id
        self.description = description
        self.start_time = None
        self.end_time = None


class TaskScheduler:
    def __init__(self):
        self.tasks = BinaryTree()

    def add_task(self, task):
        self.tasks.add(task)

    def schedule_task(self, task_id, start_time, end_time):
        task = self.tasks.search(task_id)
        task.start_time = datetime.strptime(start_time, "%d/%m/%Y %H:%M:%S")
        task.end_time = datetime.strptime(end_time, "%d/%m/%Y %H:%M:%S")

    def get_total_tasks(self):
        return f"Total tasks:\t {self.tasks.count()}"

    @staticmethod
    def get_delta(t1, t2):
        Range = namedtuple('Range', ['start', 'end'])
        r1 = Range(start=t1.start_time, end=t1.end_time)
        r2 = Range(start=t2.start_time, end=t2.end_time)
        latest_start = max(r1.start, r2.start)
        earliest_end = min(r1.end, r2.end)
        delta = (earliest_end - latest_start).total_seconds()
        return delta

    def get_conflicting_tasks(self):
        tasks = self.tasks.traverse_inorder()
        conflicting_tasks = []
        for i in range(len(tasks)):
            arr = tasks[i + 1:]
            for j in arr:
                if self.get_delta(tasks[i], j) > 0:
                    conflicting_tasks.append([tasks[i].id, j.id])
        return f"Conflicting tasks:\t {conflicting_tasks}"

    def get_longest_task(self):
        return f"Task id with longest duration:\t {max([((task.end_time - task.start_time).total_seconds(), task.id) for task in self.tasks.traverse_inorder()])[1]}"

    def get_total_duration(self):
        total_duration_in_sec = sum(
            [(task.end_time - task.start_time).total_seconds() for task in self.tasks.traverse_inorder()])
        return f"Total duration of all tasks:\t {total_duration_in_sec / 60} minutes"


if __name__ == '__main__':
    task_scheduler = TaskScheduler()
    task1 = Task(task_id=1, description="A")
    task2 = Task(task_id=2, description="B")
    task3 = Task(task_id=3, description="C")
    task4 = Task(task_id=4, description="D")
    task5 = Task(task_id=5, description="E")
    task6 = Task(task_id=6, description="F")

    for t in [task1, task2, task3, task4, task5, task6]:
        task_scheduler.add_task(t)

    schedule = [(1, "06/06/2023 09:00:00", "07/06/2023 23:59:00"), (2, "07/06/2023 09:00:00", "08/06/2023 23:59:00"),
                (3, "09/06/2023 09:00:00", "12/06/2023 23:59:00"), (4, "05/06/2023 09:00:00", "6/06/2023 13:00:00"),
                (5, "10/06/2023 09:00:00", "15/06/2023 23:59:00"), (6, "16/06/2023 00:00:00", "17/06/2023 23:59:00")]
    for t_id, st, et in schedule:
        task_scheduler.schedule_task(task_id=t_id, start_time=st, end_time=et)
    print(task_scheduler.get_total_tasks())
    print(task_scheduler.get_longest_task())
    print(task_scheduler.get_total_duration())
    print(task_scheduler.get_conflicting_tasks())

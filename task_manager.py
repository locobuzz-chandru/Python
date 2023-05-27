"""
1. TaskManager class:

    - Attributes:
        - tasks (list of Task objects)
    - Methods:
        - add_task(task): Add a new task to the task manager.
        - get_total_tasks(): Return the total number of tasks in the task manager.
        - get_completed_tasks(): Return the number of completed tasks.
        - get_incomplete_tasks(): Return the number of incomplete tasks.
        - get_overdue_tasks(): Return the number of tasks that are overdue.
        - get_tasks_by_priority(priority): Return a list of tasks with a specific priority.
        - get_tasks_by_assignee(assignee): Return a list of tasks assigned to a specific assignee.
        - complete_task(task_id): Mark a task as completed.
        - get_task_details(task_id): Return the details of a specific task.

2. Task class:

    - Attributes:

        - task_id (integer),
        - description (string),
        - priority (string),
        - assignee (string),
        - due_date (date),
        - completed (boolean)

    - Methods: None

---

#### Your task is to implement these classes and write a program to simulate the task management system.
The program should allow the user to perform the following operations:

**Add tasks to the task manager.**

-   [ ] Retrieve and display the total number of tasks.
-   [ ] Retrieve and display the number of completed tasks.
-   [ ] Retrieve and display the number of incomplete tasks.
-   [ ] Retrieve and display the number of tasks that are overdue.
-   [ ] Retrieve and display a list of tasks with a specific priority.
-   [ ] Retrieve and display a list of tasks assigned to a specific assignee.
-   [ ] Mark a task as completed.
-   [ ] Retrieve and display the details of a specific task.
"""
from datetime import datetime, date


class Task:
    def __init__(self, task_id: int, description: str, priority: str, assignee: str, due_date, completed=False):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.assignee = assignee
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        self.completed = completed


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.task_id] = task

    def get_total_tasks(self):
        return len(self.tasks)

    def get_completed_tasks(self):
        return len([tasks.task_id for tasks in self.tasks.values() if tasks.completed])

    def get_incomplete_tasks(self):
        return len([tasks.task_id for tasks in self.tasks.values() if not tasks.completed])

    def get_overdue_tasks(self):
        return sum([1 if (date.today() - task.due_date).days >= 0 else 0 for task in self.tasks.values() if
                    not task.completed])

    def get_tasks_by_priority(self, priority):
        try:
            return [task.task_id for task in self.tasks.values() if task.priority == priority]
        except:
            raise Exception("priority value does not exists")

    def complete_task(self, task_id):
        try:
            self.tasks[task_id].completed = True
        except:
            raise Exception("task id does not exists")

    def get_task_details(self, task_id):
        try:
            tsk = self.tasks[task_id]
            return f"Task ID     : {tsk.task_id}\n" \
                   f"Description : {tsk.description}\n" \
                   f"Priority    : {tsk.priority}\n" \
                   f"Assignee    : {tsk.assignee}\n" \
                   f"Due Date    : {tsk.due_date}\n" \
                   f"Completed   : {tsk.completed}"
        except:
            raise Exception("task id does not exists")


if __name__ == '__main__':
    task_manager = TaskManager()

    chandru = Task(task_id=1, description='Bank problem', priority='B', assignee='Chandru', due_date='2023-05-20')
    ravi = Task(task_id=2, description='Employee problem', priority='A', assignee='Ravi', due_date='2023-05-22')
    shuvam = Task(task_id=3, description='Django problem', priority='C', assignee='Shuvam', due_date='2023-05-25')
    milan = Task(task_id=4, description='Python problem', priority='A', assignee='Milan', due_date='2023-05-26')
    ajay = Task(task_id=5, description='HTML problem', priority='B', assignee='Ajay', due_date='2023-05-27')

    for t in [chandru, ravi, shuvam, milan, ajay]:
        task_manager.add_task(t)
    # print(task_manager.get_total_tasks())
    # print(task_manager.get_completed_tasks())
    # print(task_manager.get_incomplete_tasks())
    # print(task_manager.get_overdue_tasks())
    # print(task_manager.get_tasks_by_priority(priority='A'))
    # print(task_manager.complete_task(5))
    print(task_manager.get_task_details(1))

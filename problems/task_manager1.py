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
    def __init__(self, task=None):
        self.task = task
        self.left = None
        self.right = None

    def add_task(self, task):
        if self.task is None:
            self.task = task
            return
        if self.task == task:
            return
        if task.task_id < self.task.task_id:
            if self.left is None:
                self.left = TaskManager(task)
            else:
                self.left.add_task(task)
        else:
            if self.right is None:
                self.right = TaskManager(task)
            else:
                self.right.add_task(task)

    def total_tasks(self, task):
        if task is None:
            return 0
        return 1 + self.total_tasks(task.left) + self.total_tasks(task.right)

    def complete_task(self, task_id):
        if self.task is None:
            return
        elif self.task.task_id == task_id:
            self.task.completed = True
            return
        elif task_id < self.task:
            if self.left is None:
                return
            else:
                self.left.search(task_id)
        else:
            if self.right is None:
                return
            else:
                self.right.search(task_id)

    def preorder(self, result: list):
        result.append(self.task)
        if self.left:
            self.left.preorder(result)
        if self.right:
            self.right.preorder(result)
        return result

    def get_completed_tasks(self):
        result = []
        self.preorder(result)
        return len([task.task_id for task in result if task.completed])

    def get_incomplete_tasks(self):
        result = self.preorder([])
        return len([tasks.task_id for tasks in result if not tasks.completed])

    def get_overdue_tasks(self):
        result = self.preorder([])
        return sum([1 if (date.today() - task.due_date).days >= 0 else 0 for task in result if not task.completed])

    def get_tasks_by_priority(self, priority):
        result = self.preorder([])
        return [task.task_id for task in result if task.priority == priority]

    def get_task_details(self, task_id):
        if self.task is None:
            return
        elif self.task.task_id == task_id:
            return f"Task ID     : {self.task.task_id}\n" \
                   f"Description : {self.task.description}\n" \
                   f"Priority    : {self.task.priority}\n" \
                   f"Assignee    : {self.task.assignee}\n" \
                   f"Due Date    : {self.task.due_date}\n" \
                   f"Completed   : {self.task.completed}"

        elif task_id < self.task:
            if self.left is None:
                return
            else:
                self.left.search(task_id)
        else:
            if self.right is None:
                return
            else:
                self.right.search(task_id)


if __name__ == '__main__':
    task_manager = TaskManager()
    milan = Task(task_id=4, description='Python problem', priority='A', assignee='Milan', due_date='2023-05-26')
    ravi = Task(task_id=2, description='Employee problem', priority='A', assignee='Ravi', due_date='2023-05-22')
    chandru = Task(task_id=1, description='Bank problem', priority='B', assignee='Chandru', due_date='2023-05-20')
    shuvam = Task(task_id=3, description='Django problem', priority='C', assignee='Shuvam', due_date='2023-05-25')
    ajay = Task(task_id=5, description='HTML problem', priority='B', assignee='Ajay', due_date='2023-05-27')

    for t in [chandru, ravi, shuvam, milan, ajay]:
        task_manager.add_task(t)

    # print(task_manager.total_tasks(task_manager))
    # print(task_manager.get_overdue_tasks())
    # print(task_manager.get_tasks_by_priority('B'))
    # print(task_manager.get_completed_tasks())
    # print(task_manager.get_incomplete_tasks())
    task_manager.complete_task(1)
    # print(task_manager.get_completed_tasks())
    # print(task_manager.get_incomplete_tasks())
    print(task_manager.get_task_details(1))

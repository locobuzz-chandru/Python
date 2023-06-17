from datetime import datetime, date
from bst import BinaryTree


class Task:
    def __init__(self, task_id: int, description: str, priority: str, assignee: str, due_date, completed=False):
        self.id = task_id
        self.description = description
        self.priority = priority
        self.assignee = assignee
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        self.completed = completed


class TaskManager:
    def __init__(self):
        self.tasks = BinaryTree()

    def add_task(self, task):
        self.tasks.add(task)

    def total_tasks(self):
        return self.tasks.count()

    def _get_tasks(self):
        return self.tasks.traverse_inorder()

    def get_completed_tasks(self):
        return len([task.id for task in self._get_tasks() if task.completed])

    def get_incomplete_tasks(self):
        return len([tasks.id for tasks in self._get_tasks() if not tasks.completed])

    def get_overdue_tasks(self):
        return sum([1 if (date.today() - task.due_date).days >= 0 else 0 for task in self._get_tasks() if
                    not task.completed])

    def get_tasks_by_priority(self, priority):
        tasks = [task.id for task in self._get_tasks() if task.priority == priority]
        if tasks:
            return tasks
        raise Exception("priority value does not exist")

    def _get_task_by_id(self, task_id):
        task = self.tasks.search(task_id)
        if task:
            return task
        raise Exception("task id does not exist")

    def complete_task(self, task_id):
        self._get_task_by_id(task_id).completed = True

    def get_task_details(self, task_id):
        try:
            tsk = self._get_task_by_id(task_id)
            return f"Task ID     : {tsk.id}\n" \
                   f"Description : {tsk.description}\n" \
                   f"Priority    : {tsk.priority}\n" \
                   f"Assignee    : {tsk.assignee}\n" \
                   f"Due Date    : {tsk.due_date}\n" \
                   f"Completed   : {tsk.completed}"
        except:
            raise Exception("task id does not exists")


if __name__ == '__main__':
    task_manager = TaskManager()
    milan = Task(task_id=4, description='Python problem', priority='A', assignee='Milan', due_date='2023-05-26')
    ravi = Task(task_id=2, description='Employee problem', priority='A', assignee='Ravi', due_date='2023-05-22')
    chandru = Task(task_id=1, description='Bank problem', priority='B', assignee='Chandru', due_date='2023-05-20')
    shuvam = Task(task_id=3, description='Django problem', priority='C', assignee='Shuvam', due_date='2023-05-25')
    ajay = Task(task_id=5, description='HTML problem', priority='B', assignee='Ajay', due_date='2023-05-27')

    for t in [chandru, ravi, shuvam, milan, ajay]:
        task_manager.add_task(t)

    print(task_manager.total_tasks())
    print(task_manager.get_overdue_tasks())
    print(task_manager.get_tasks_by_priority('B'))
    print(task_manager.get_completed_tasks())
    print(task_manager.get_incomplete_tasks())
    task_manager.complete_task(1)
    print(task_manager.get_completed_tasks())
    print(task_manager.get_incomplete_tasks())
    print(task_manager.get_task_details(2))

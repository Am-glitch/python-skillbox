import itertools

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items == 0)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    

class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.push((task, priority))

    def __str__(self):
        sorted_tasks = sorted(self.tasks.items, key=lambda x: x[1])
        result = ""
        for priority, group in itertools.groupby(sorted_tasks, key=lambda x: x[1]):
            tasks = "; ".join(task for task, _ in group)
            result += f"{priority} — {tasks}\n"
        return result

manager = TaskManager()

manager.new_task("do smth", 4)
manager.new_task("do smth more", 4)
manager.new_task("chill", 2)

print(manager)

#Task Management System
import heapq
class TaskManager:
    def __init__(self, tasks):
        self.heap = []
        self.task_map = {}
        self.removed = set()
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)
    def add(self, userId, taskId, priority):
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))
    def edit(self, taskId, newPriority):
        if taskId not in self.task_map:
            return
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))
    def rmv(self, taskId):
        if taskId in self.task_map:
            self.removed.add((taskId, self.task_map[taskId][1]))
            del self.task_map[taskId]
    def execTop(self):
        while self.heap:
            neg_priority, negTaskId, taskId = heapq.heappop(self.heap)
            actual_priority = -neg_priority
            if (taskId, actual_priority) in self.removed:
                self.removed.remove((taskId, actual_priority))
                continue
            if taskId not in self.task_map:
                continue
            userId, current_priority = self.task_map[taskId]
            if current_priority != actual_priority:
                continue
            del self.task_map[taskId]
            return userId
        return -1
n = int(input("Enter number of initial tasks: "))
print("Enter each task as: userId taskId priority")
for _ in range(n):
    userId, taskId, priority = map(int, input().split())
    tasks.append([userId, taskId, priority])
tm = TaskManager(tasks)
while True:
    op = input("Enter operation (add/edit/rmv/execTop/exit): ").strip()
    if op == "exit":
        break
    elif op == "add":
        userId, taskId, priority = map(int, input("Enter userId taskId priority: ").split())
        tm.add(userId, taskId, priority)
        print("Added.")
    elif op == "edit":
        taskId, newPriority = map(int, input("Enter taskId newPriority: ").split())
        tm.edit(taskId, newPriority)
        print("Edited.")
    elif op == "rmv":
        taskId = int(input("Enter taskId to remove: "))
        tm.rmv(taskId)
        print("Removed.")
    elif op == "execTop":
        res = tm.execTop()
        print("Executed task's userId:", res)
    else:
        print("Invalid operation.")

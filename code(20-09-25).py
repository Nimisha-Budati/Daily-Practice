#Router implementation
from collections import deque, defaultdict
import bisect
class Router:
    def __init__(self, memoryLimit):
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.seen = set()
        self.dest_map = defaultdict(list)  
    def addPacket(self, source, destination, timestamp):
        packet = (source, destination, timestamp)
        if packet in self.seen:
            return False
        if len(self.queue) == self.memoryLimit:
            old_packet = self.queue.popleft()
            self.seen.remove(old_packet)
            old_dst, old_time = old_packet[1], old_packet[2]
            idx = bisect.bisect_left(self.dest_map[old_dst], old_time)
            self.dest_map[old_dst].pop(idx)
        self.queue.append(packet)
        self.seen.add(packet)
        bisect.insort(self.dest_map[destination], timestamp)
        return True
    def forwardPacket(self):
        if not self.queue:
            return []
        packet = self.queue.popleft()
        self.seen.remove(packet)
        dst, time = packet[1], packet[2]
        idx = bisect.bisect_left(self.dest_map[dst], time)
        self.dest_map[dst].pop(idx)
        return list(packet)
    def getCount(self, destination, startTime, endTime):
        arr = self.dest_map[destination]
        left = bisect.bisect_left(arr, startTime)
        right = bisect.bisect_right(arr, endTime)
        return right - left
router = None
flag = True
while flag:
    cmd = input("Enter command (or x to exit): ")
    if cmd.strip() == "x":
        flag = False
    else:
        parts = cmd.strip().split()
        if not parts:
            continue
        if parts[0] == "Router":
            router = Router(int(parts[1]))
            print("null")
        elif parts[0] == "addPacket":
            res = router.addPacket(int(parts[1]), int(parts[2]), int(parts[3]))
            print(str(res).lower())
        elif parts[0] == "forwardPacket":
            print(router.forwardPacket())
        elif parts[0] == "getCount":
            res = router.getCount(int(parts[1]), int(parts[2]), int(parts[3]))
            print(res)

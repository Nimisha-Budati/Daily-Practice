import heapq
class MovieRentingSystem:
    def __init__(self, n, entries):
        self.price = {}
        self.available = {}
        self.is_available = {}
        self.rented = set()
        self.report_heap = []
        self.rent_id = {}
        self.cur_id = 0
        for s, m, p in entries:
            self.price[(s, m)] = p
            self.is_available[(s, m)] = True
            if m not in self.available:
                self.available[m] = []
            heapq.heappush(self.available[m], (p, s))

    def search(self, movie):
        res = []
        if movie not in self.available:
            return res
        temp = []
        seen = set()
        while self.available[movie] and len(res) < 5:
            p, s = heapq.heappop(self.available[movie])
            if not self.is_available.get((s, movie), False):
                continue
            if s in seen:
                continue
            res.append(s)
            seen.add(s)
            temp.append((p, s))
        for item in temp:
            heapq.heappush(self.available[movie], item)
        return res

    def rent(self, shop, movie):
        self.rented.add((shop, movie))
        self.is_available[(shop, movie)] = False
        self.cur_id += 1
        self.rent_id[(shop, movie)] = self.cur_id
        heapq.heappush(self.report_heap, (self.price[(shop, movie)], shop, movie, self.cur_id))

    def drop(self, shop, movie):
        if (shop, movie) in self.rented:
            self.rented.remove((shop, movie))
        self.is_available[(shop, movie)] = True
        self.rent_id.pop((shop, movie), None)
        heapq.heappush(self.available[movie], (self.price[(shop, movie)], shop))

    def report(self):
        res = []
        temp = []
        while self.report_heap and len(res) < 5:
            p, s, m, rid = heapq.heappop(self.report_heap)
            if (s, m) in self.rented and self.rent_id.get((s, m), None) == rid:
                res.append([s, m])
                temp.append((p, s, m, rid))
        for item in temp:
            heapq.heappush(self.report_heap, item)
        return res

n = int(input("Enter number of shops: "))
entries = []
e = int(input("Enter number of movie entries: "))
print("Enter entries as: shop movie price")
for _ in range(e):
    s, m, p = map(int, input().split())
    entries.append([s, m, p])

mrs = MovieRentingSystem(n, entries)

while True:
    cmd = input("Enter command (search/rent/drop/report/exit): ").strip().lower()
    if cmd == "exit":
        break
    if cmd == "search":
        movie = int(input("Enter movie id to search: "))
        print(mrs.search(movie))
    elif cmd == "rent":
        shop, movie = map(int, input("Enter shop and movie id to rent: ").split())
        mrs.rent(shop, movie)
        print("Rented")
    elif cmd == "drop":
        shop, movie = map(int, input("Enter shop and movie id to drop: ").split())
        mrs.drop(shop, movie)
        print("Dropped")
    elif cmd == "report":
        print(mrs.report())
    else:
        print("Invalid command")

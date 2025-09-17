#Optimize FoodRatings system with heap to prevent TLE
#used list which caused TLE on large inputs
import heapq
class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_map = {}  
        self.cuisine_heap = {} 
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_map[f] = [r, c]
            if c not in self.cuisine_heap:
                self.cuisine_heap[c] = []
            heapq.heappush(self.cuisine_heap[c], (-r, f))
    def changeRating(self, food, newRating):
        c = self.food_map[food][1]
        self.food_map[food][0] = newRating
        heapq.heappush(self.cuisine_heap[c], (-newRating, food))
        return "null"
    def highestRated(self, cuisine):
        heap = self.cuisine_heap[cuisine]
        while True:
            r, f = heap[0]
            if -r == self.food_map[f][0]:
                return f
            else:
                heapq.heappop(heap)
n = int(input("Enter number of foods: "))
foods = []
cuisines = []
ratings = []
for _ in range(n):
    f, c, r = input("Enter food, cuisine, rating separated by space: ").split()
    foods.append(f)
    cuisines.append(c)
    ratings.append(int(r))
food_ratings = FoodRatings(foods, cuisines, ratings)
while True:
    query = input("Enter query (changeRating/ highestRated/ exit): ").strip()
    if query == "exit":
        break
    elif query == "changeRating":
        f, r = input("Enter food and new rating: ").split()
        print(food_ratings.changeRating(f, int(r)))
    elif query == "highestRated":
        c = input("Enter cuisine: ").strip()
        print(food_ratings.highestRated(c))
    else:
        print("Invalid query!")

"""
k nearest star

Basic idea: find the k-closest stars to earth

store K stars in heap, evict largest star, continue adding until you’ve
gone throw all the starts.

Then print the K closest stars

n log (k)

how to add a start to a heap?
"""
import heapq


class Star:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property    
    def distance(self):
        return -(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance
    def __str__(self):
        return str([self.x,self.y,self.z])


def k_closest(distances, k):
    h = []
    print("distances are", distances)
    print("initializing heap with values:")
    for i in range(k):
        temp = Star(distances[i][0], distances[i][1], distances[i][2])
        print(temp)
        heapq.heappush(h, temp)

    print('adding and popping remaining values:')
        
    for i in range(k, len(distances)):
        temp = Star(distances[i][0], distances[i][1], distances[i][2])
        print('pushing', temp)
        heapq.heappush(h, temp)
        print('popping', heapq.heappop(h))
        
    return h

if __name__ == '__main__':
    distances=[(0, 0, 1), (1, 0, 1), (3, 35, 15), (0, 1, 0), (100, 500, 20)]
    h = k_closest(distances, 3)
    print('final heap:')
    for item in h:
        print(item)

'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/
'''

import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for from_city, to_city, price in flights:
            graph[from_city].append((to_city, price))

        pq = [(0, src, 0)]

        visited = {}

        while pq:
            cost, city, stops = heapq.heappop(pq)
            
            if city == dst:
                return cost

            if stops > k:
                continue

            if city in visited and visited[city] <= stops:
                continue

            visited[city] = stops

            for neighbor, price in graph[city]:
                heapq.heappush(pq, (cost + price, neighbor, stops + 1))

        return -1
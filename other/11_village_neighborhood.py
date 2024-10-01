'''
There are n villages located at distinct points on a straight road. Each village
is represented by an integer that indicates its position on the road.

A village’s left neighbor is the village with the next smallest position;
a village’s right neighbor is the village with the next biggest position. The
neighborhood of a village consists of half the space between that village and its
left neighbor, plus half the space between that village and its right neighbor.

For example, if there’s a village at position 10, with its left neighbor at position 6 and its right neighbor at position 15, then this village’s neighborhood
starts from position 8 (halfway between 6 and 10) and ends at position 12.5
(halfway between 10 and 15).

The leftmost and rightmost villages have only one neighbor, so the definition of a neighborhood doesn’t make sense for them. We’ll ignore the
neighborhoods of those two villages in this problem.

neighborhood that goes from 8 to 12.5 has size 12.5 – 8 = 4.5.

Determine the size of the smallest neighborhood.
'''
n = int(input())

positions = []

for i in range(n):
    positions.append(int(input()))

positions.sort()

left = (positions[1] - positions[0]) / 2
right = (positions[2] - positions[1]) / 2

min_size = left + right

for i in range(2, n - 1):
    left = (positions[i] - positions[i - 1]) / 2
    right = (positions[i + 1] - positions[i]) / 2
    size = left + right
    if size < min_size:
        min_size = size

print(min_size)

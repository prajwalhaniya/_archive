"""
# Calculate the volume of a right circular cone.

input:
The input consists of two lines of text. The first line contains integer r, the radius of the cone. The second line contains integer h, the height of the cone. Both r and h are between 1 and 100. (That is, the minimum value for r and h is 1, and the maximum value is 100)

output:
Output the volume of the right circular cone with radius r and height h. The formula to calculate the volume is (πr^2h)/3.
"""

PI = 3.141592653589793
r = int(input())
h = int(input())

result = (PI * r ** 2 * h) / 3

print(result)

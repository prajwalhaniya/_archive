'''
Pero has a data plan with his cell phone provider that offers him x megabytes
of data per month. In addition, any data he doesn’t use in a given month
carries over to the next month. For example, if x is 10 and Pero uses only
4MB in a given month, the remaining 6MB carry over to the next month (in
which he’d now have 10 + 6 = 16MB available).
We’re given the number of megabytes of data that Pero uses in each of
the first n months. Our task is to determine the number of megabytes available for the following month.
'''

monthly_mb = int(input())
n = int(input())

excess = 0

for i in range(n):
    used = int(input())
    excess = excess + monthly_mb - used

print(excess, 'mb is remaining')
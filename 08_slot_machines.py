'''
Martha goes to a casino and brings n quarters. The casino has three slot machines, and she plays them in order until she has no quarters left. That is,
she plays the first slot machine, then the second, then the third, then back to
the first, then the second, and so on. Each play costs one quarter.
The slot machines operate according to the following rules:

• The first slot machine pays 30 quarters every 35th time it is played.
• The second slot machine pays 60 quarters every 100th time it is
played.
• The third slot machine pays 9 quarters every 10th time it is played.
• No other plays pay anything.
Determine the number of times Martha plays before she has no quarters
left.

'''

quarters = int(input())
first = int(input())
second = int(input())
third = int(input())

plays = 0
machine = 0

while quarters >= 1:
    quarters = quarters - 1

    if machine == 0:
        first += 1
        if first == 35:
            first = 0
            quarters += 30
    elif machine == 1:
        second += 1
        if second == 100:
            second = 0
            quarters += 60
    elif machine == 2:
        third += 1
        if third == 10:
            third = 0
            quarters += 9
    
plays += 1
machine += 1

if machine == 3:
    machine = 0

print('Martha plays', plays, 'times before going broke.')
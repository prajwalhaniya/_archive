'''
Borko has a row of three opaque cups: one at the left (location 1), one at the middle (location 2), and one at the right (location 3). There is a ball under the cup at the left. It’s our job to keep track of the location of the ball as Borko swaps the locations of the cups. Borko can make three types of swap:

A Swap the left and middle cups
B Swap the middle and right cups
C Swap the left and right cups

Input:
The input is one line of at most 50 characters. Each character specifies a type of swap that Borko makes: A, B, or C.

Output:

Output the final location of the ball:

• 1 if the ball is at the left
• 2 if the ball is at the middle
• 3 if the ball is at the right
'''

swaps = input()
ball_location = 1

for swap_type in swaps:
    if swap_type == 'A' and ball_location == 1:
        ball_location = 2
    elif swap_type == 'A' and ball_location == 2:
        ball_location = 1
    elif swap_type == 'B' and ball_location == 2:
        ball_location = 3
    elif swap_type == 'B' and ball_location == 3:
        ball_location = 2
    elif swap_type == 'C' and ball_location == 1:
        ball_location = 3
    elif swap_type == 'C' and ball_location == 3:
        ball_location = 1

print(ball_location)
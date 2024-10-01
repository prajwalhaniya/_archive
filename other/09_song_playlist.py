'''
We have five favorite songs named A, B, C, D, and E. We’ve created a playlist
of these songs and are using an app to manage the playlist. The songs start
off in the order A, B, C, D, E. The app has four buttons:

• Button 1: Moves the first song of the playlist to the end of the playlist. For example, if the playlist is currently A, B, C, D, E, then it
changes to B, C, D, E, A.

• Button 2: Moves the last song of the playlist to the beginning of the
playlist. For example, if the playlist is currently A, B, C, D, E, then it
changes to E, A, B, C, D.

• Button 3: Swaps the first two songs of the playlist. For example,
if the playlist is currently A, B, C, D, E, then it changes to be B, A,
C, D, E.

• Button 4: Plays the playlist!

We’re provided a user’s button presses. When the user presses button 4,
output the order of songs in the playlist.
'''

songs = 'ABCDE'

button = 0

while button != 4:
    button = int(input())
    presses = int(input())
    for i in range(presses):
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:]

output = ''

for song in songs:
    output = output + song + ''

print(output)

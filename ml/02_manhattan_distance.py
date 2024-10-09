users = {
  "Angelica": {
    "Blues Traveler": 3.5,
    "Broken Bells": 2,
    "Norah Jones": 4.5,
    "Phoenix": 5,
    "Slightly Stoopid": 1.5,
    "The Strokes": 2.5,
    "Vampire Weekend": 2
  },
  "Bill": {
    "Blues Traveler": 2,
    "Broken Bells": 3.5,
    "Deadmau5": 4,
    "Phoenix": 2,
    "Slightly Stoopid": 3.5,
    "Vampire Weekend": 3
  },
  "Chan": {
    "Blues Traveler": 5,
    "Broken Bells": 1,
    "Deadmau5": 1,
    "Norah Jones": 3,
    "Phoenix": 5,
    "Slightly Stoopid": 1
  },
  "Dan": {
    "Blues Traveler": 3,
    "Broken Bells": 4,
    "Deadmau5": 4.5,
    "Phoenix": 3,
    "Slightly Stoopid": 4.5,
    "The Strokes": 4,
    "Vampire Weekend": 2
  },
  "Hailey": {
    "Broken Bells": 4,
    "Deadmau5": 1,
    "Norah Jones": 4,
    "The Strokes": 4,
    "Vampire Weekend": 1
  },
  "Jordyn": {
    "Broken Bells": 4.5,
    "Deadmau5": 4,
    "Norah Jones": 5,
    "Phoenix": 5,
    "Slightly Stoopid": 4.5,
    "The Strokes": 4,
    "Vampire Weekend": 4
  },
  "Sam": {
    "Blues Traveler": 5,
    "Broken Bells": 2,
    "Norah Jones": 3,
    "Phoenix": 5,
    "Slightly Stoopid": 4,
    "The Strokes": 5
  },
  "Veronica": {
    "Blues Traveler": 3,
    "Norah Jones": 5,
    "Phoenix": 4,
    "Slightly Stoopid": 2.5,
    "The Strokes": 3
  }
}

def manhattan_distance(rating_1, rating_2):
    distance = 0
    for key in rating_1:
        if key in rating_2:
            distance += abs(rating_1[key] - rating_2[key])
    return distance

result = manhattan_distance(users["Hailey"], users["Veronica"])
print(result)

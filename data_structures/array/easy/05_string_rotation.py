def is_substring(s1, s2):
    return s2 in s1

def isRotation(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False

    concatenated = s1 + s1

    return is_substring(concatenated, s2) 

s1 = "waterbottle"
s2 = "erbottlewat"
print(isRotation(s1, s2)) 
'''
https://leetcode.com/problems/longest-palindrome/description/
'''
def longest_palindrome(s: str) -> int:
    from collections import Counter

    # Count the frequency of each character
    char_counts = Counter(s)
    length = 0
    odd_found = False

    for count in char_counts.values():
        # Add the largest even number <= count
        length += count // 2 * 2
        # Check if there is at least one odd count
        if count % 2 == 1:
            odd_found = True

    # Add 1 if there is at least one character with an odd count
    if odd_found:
        length += 1

    return length
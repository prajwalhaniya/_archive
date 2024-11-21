def is_palindrome(s: str) -> bool:
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False  # Not a palindrome
        left += 1
        right -= 1
    
    return True  # Is a palindrome

# Example usage:
test_strings = ["A man, a plan, a canal: Panama", "racecar", "hello"]
for test in test_strings:
    print(f'"{test}" is a palindrome: {is_palindrome(test)}')
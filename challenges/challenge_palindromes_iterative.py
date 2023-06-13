def is_palindrome_iterative(word):
    if word is None:
        return False

    if len(word) == 0:
        return False

    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True

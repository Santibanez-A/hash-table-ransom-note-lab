def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # TODO: Implement this function
    letter_counts = {}

    for letter in magazine:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    for letter in ransomNote:
        if letter not in letter_counts or letter_counts[letter] == 0:
            return False

        letter_counts[letter] -= 1

    return True
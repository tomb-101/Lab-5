def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...

    count=0

    for letter in str1:
        if letter in str2:
            count+=1
    
    if count==len(str2) and len(str1)==len(str2):
        return True
    else:
        return False

## Example 
# print(are_anagrams("listen", "silent"))  # Expected output: True
# print(are_anagrams("hello", "world"))    # Expected output: False

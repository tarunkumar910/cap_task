# WAP to count the number of vowels in a string using a for loop.

import logging

logging.basicConfig(
    filename='vowel_count.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def count_vowels(s:str) -> int:
    """
    Count the number of vowels in a given string.

    Parameters:
        s (str): Input string

    Returns:
        int: Total number of vowels in the string.
    """
    count = 0
    for char in s:
        if char in 'aeiouAEIOU':
            count += 1
        logging.info(f"Current character: {char}, Vowel count: {count}")
    return count

s = "Hello World"
vowel_count = count_vowels(s)  
print(f"Number of vowels in '{s}': {vowel_count}")

# WAP to print the frequency of each character

import logging

logging.basicConfig(
    filename='char_freq.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def char_freq(s:str) -> dict:
    """
    Count the frequency of each character in a given string.

    Parameters:
        s (str): Input string

    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """

    freq={}
    for char in s:
        if char != ' ':
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1

        logging.info(f"Current character: {char}, Frequency: {freq.get(char, 0)}")  
    return freq

s="Hello World"
frequency = char_freq(s)
print(f"Character frequency in '{s}': {frequency}")

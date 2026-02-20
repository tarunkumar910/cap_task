# WAP to find the second largest number in a list.

import logging

logging.basicConfig(
    filename='second_largest.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def second_largest(nums:list)-> int:
    """
    Find the Second largest element

    Parameters:
      nums(list): Input List

    Return: 
        second: A second largest element from the list
    """
    second = 0
    largest = 0
    for num in nums:
        if num > second and num < largest:
            second = num
        elif num > largest:
            second = largest
            largest = num

        logging.info(f"Current number: {num}, Largest: {largest}, Second Largest: {second}")    

    return second

numbers = [3, 5, 7, 2, 8]
result = second_largest(numbers)
print(f"The second largest number in the list is: {result}")

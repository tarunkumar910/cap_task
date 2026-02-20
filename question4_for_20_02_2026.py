# WAP to check whether a list is sorted or not

import logging

logging.basicConfig(
    filename='check_sorted.log',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_ascending(nums:list)->bool:
    """
    Check whether a list is sorted in ascending order.

    Parameters:
        nums (list): Input list of numbers

    Returns:
        bool: True if the list is sorted in ascending order, False otherwise.
    """
    prev=nums[0]
    for num in nums:
        if prev <= num:
            prev=num
        else :
            logging.info(f"List: {nums}, Sorted in ascending order: {False}")
            return False

    logging.info(f"List: {nums}, Sorted in ascending order: {True}")
    return True

nums=[1,2,3,5,6,4]
print(check_ascending(nums))

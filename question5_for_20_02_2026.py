import logging

logging.basicConfig(
    filename='revers.log',
    level=logging.INFO,
    format ="%(asctime)s - %(levelname)s - %(message)s"
 )

def revrse_string(s:str)->str:
    """
    Revers the string without the slicing 
    Parmeters:
      s(str): input the string
    Result:
      a(str):revrse the input string
    """
    a=""
    for char in s:
        a=char+a
        logging.info(f"the orginal string {s} and reverse string {a}")

    
revrse_string("tarun")

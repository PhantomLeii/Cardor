from utils import *
import sys

def main():
    # Get card number
    try:
        number = sys.argv[1]
    except Exception as e:
        print(
            "Input must be a number.\nFailed with error: {}".format(e)
        )
        return 1
    
    # Convert number to Tuple[int]
    number = split_number(number)

    # Run 3 tests simultaneously
    # Check american express validity
    if get_first_number(number) == 34 or get_first_number(number) == 37:
        if len(number) != 15 or not luhn_compliant(number):
            print("INVALID")
            return -1
        
        print("AMEX")
        return 0

    elif get_first_number(number) >= 51 and get_first_number <= 55:
        if len(number) != 16 or not luhn_compliant(number):
            print("INVALID")
            return -1
        
        print("MASTERCARD")
        return 0
    
    elif str(get_first_number(number)).startswith("4"):
        if len(number) not in (13, 16) or not luhn_compliant(number):
            print("INVALID")
            return -1
        
        print("VISA")
        return 0
    
    print("INVALID")      

if __name__ == "__main__":
    main()
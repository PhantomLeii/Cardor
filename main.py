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

    # Run test
    if get_first_number(number) == 34 or get_first_number(number) == 37:
        if is_valid(number, 15) is False:
            print("INVALID")
            return 0

        print("AMEX")
        return 0

    elif get_first_number(number) >=51 and get_first_number(number) <= 55:
        if is_valid(number, 16) is False:
            print("INVALID")
            return 0
        
        print("MASTERCARD")
        return 0
    
    elif get_first_number(number) == 4:
        if is_valid(number, (13, 16)) is False:
            print("INVALID")
            return 0
        
        print("VISA")
        return 0

if __name__ == "__main__":
    main()
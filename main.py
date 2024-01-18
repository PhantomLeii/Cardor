from utils import *
import sys

def main():
    # Prompt user for card number
    card_number = sys.argv[1].strip()
    
    number = list([int(i) for i in card_number])

    # Check if valid AMEX card
    if get_first_number(number=number) == 34 or get_first_number(number=number) == 37:
        if len(number) != 15 or luhn_compliant(number) is False:
            print("INVALID")
            return 0
        print("AMEX")
        return 0
    
    # Check if valid MASTERCARD
    elif get_first_number(number=number) >= 51 and get_first_number(number=number) <= 55:
        if len(number) != 16 or luhn_compliant(number=number) is False:
            print("INVALID")
            return 0
        print("MASTERCARD")
        return 0
    
    # Check if valid VISA card
    elif get_first_number(number=number) == 4:
        lengths = (13, 16)
        if len(number) not in lengths or luhn_compliant(number) is False:
            print("INVALID")
            return 0
        print("VISA")
        return 0
    
    else:
        print("INVALID")
        return 0

if __name__ == "__main__":
    main()
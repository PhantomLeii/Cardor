from utils import *
import sys

def main():
    # Prompt user for card number
    card_number = "4847954053662521"
    
    number = list([int(i) for i in card_number])

    # Check card number validity
    first_number = get_first_number(number=number)
    number_length = len(number)
    
    if first_number == 34 or first_number == 37:
        if not luhn_compliant(number) or number_length(number) != 16:
            print("INVALID")
            return 0
        print("AMEX")
        return 0
    
    elif first_number >= 51 and first_number <= 55:
        if not luhn_compliant(number) or number_length != 15:
            pass

    # Print card type
    return 0

if __name__ == "__main__":
    main()
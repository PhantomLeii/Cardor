import utils
import sys

def main():
    # Get card number
    try:
        number = int(sys.argv[2])
    except Exception as e:
        print("Input must be a number.\n\nFailed with error: {}".format(e))
    
    # Convert number to tuple with int digits for easy maths
    print(utils.split_number(number))

    pass

if __name__ == "__main__":
    main()
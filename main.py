import utils
import sys

def main():
    # Get card number
    try:
        number = sys.argv[1]
        # Convert number to Tuple[int]
        number = utils.split_number(number)
    except Exception as e:
        print(
            "Input must be a number.\nFailed with error: {}".format(e)
        )

    pass

if __name__ == "__main__":
    main()
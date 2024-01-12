from utils import Card

def main():
    # prompt user for card number
    name = str(input("Name (Default = Card): "))
    try:
        card_number = int(input("Card Number: "))
    except Exception as e:
        print(f"Error: {e}\nInput has to be a number")
        

    # create instance of Card
    # Validate card through all methods
    pass

if __name__ == "__main__":
    main()
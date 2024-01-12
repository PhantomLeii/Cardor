from utils import Card

def main():
    # prompt user for card number
    name = str(input("Name (Default = Card): "))
    try:
        card_number = int(input("Card Number: "))
    except Exception as e:
        print(f"Error: {e}\nInput has to be a number")
        pass
        
        # 4293021017275607
    # create instance of Card
    card = Card(card_number, name)
    # Validate card through all methods
    print(card)

if __name__ == "__main__":
    main()
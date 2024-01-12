class Card:
    def __init__(
            self,
            card_number,
            name="Card"
    ):
        """
        Use card number to automatically verify
        card is a valid card
        :param name: Arbitrary name given to card.
        :param card_number: Unique card number.
        """
        self.name = name
        self.card_number = card_number

        # Validate card number
        assert self.__is_valid(self.card_number), "INVALID"
    
    def __str__(self) -> str:
        """Default instance as string of card name."""
        return self.name
    
    @staticmethod
    def __is_valid(number):
        """Validate card number using length."""
        card_lengths = (13, 15, 16)
        if not len(number) in card_lengths:
            return False
        
        return True
    
    def setName(self, new_name):
        """Set a new name for the card in question."""
        self.name = new_name
        pass

    def get_first_number(self):
        """Isolate the first 2 numbers"""
        number = self.card_number
        while number > 100:
            number /= 10
        
        return number
    
    def count_digits(self):
        """Count number of digits"""
        number = self.card_number
        i = 0
        for digit in number:
            i += 1
        
        return i
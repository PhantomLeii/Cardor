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
    
    def __str__(self) -> str:
        return self.name
    
    def setName(self, new_name):
        """Set a new name for the card in question."""
        self.name = new_name
        pass


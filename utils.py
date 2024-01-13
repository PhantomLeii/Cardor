"""
Global functions required by Cardor for card number verification.
"""

def split_number(number):
    num_data = tuple(str(number).split())
    return (int(i) for i in num_data)
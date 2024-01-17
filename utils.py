"""
Global functions & structures required by Cardor for card number verification.
"""

# CONSTANTS = {
#     "amex": (
#         (15,), # digits
#         (34, 37) # startswith
#     ),

#     "mastercard": (
#         (16,),
#         (51, 52, 52, 54, 55)
#     ),

#     "visa": (
#         (13, 16),
#         (4,)
#     )
# }

def split_number(number:iter) -> tuple:
    store = []
    for i in number:
        store.append(int(i))
    return tuple(store)

def get_first_number(num:iter):
    return int(str(num[0]) + str(num[1]))

def digit_sum(val:int) -> int:
    digit_sum = 0
    if val > 9:
        digit_sum += sum([int(i) for i in str(val).split()])
    else:
        digit_sum = val
    
    return digit_sum

def luhn_compliant(num:iter) -> bool:
    score = [0,0] # every_other, not_multiplied
    count = 0
    for i in num:
        count += 1
        if count % 2 == 0:
            product = i * 2
            score[0] += digit_sum(product)
        else:
            score[1] += i

    if sum(score) % 10 == 0:
        return True
    else:
        return False

def get_first_number(number):
    """Isolate the first 2 numbers or number if number starts with 4"""
    if number[0] == 4:
        return number[0]
    
    first_number = int(str(number[0]) + str(number[1]))
    return first_number

def digit_sum(val):
    """Calculate the sum of the digits in a number"""
    digit_sum = 0
    if val > 9:
        digits = str(val)
        digit_sum += (int(digits[0]) + int(digits[1]))
    else:
        digit_sum = val
    
    return digit_sum

def luhn_compliant(number):
    """Check if number complies with luhn algorithm rule"""
    rev_number = number.reverse() # Reverse given card number
    
    score = [0, 0] # every_other, not_multiplied
    count = 0
    for i in number:
        count += 1
        if count % 2 == 0:
            product = i * 2
            score[0] += digit_sum(product)
        else:
            score[1] += i
        
    if sum(score) % 10 == 0:
        return True
    
    return False
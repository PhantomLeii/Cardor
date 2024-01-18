# Cardor

I started self-studying some computer science with materials and resources gathered by a community known as the (Open Source Society University (OSSU))[https://ossu.dev/]. They've compiled something really comprehensive, do have a look at what they have to offer. The project demonstrated here is an idea I got from the CS50x course hosted by (Harvard University)[https://harvard/] among all the courses and learning resources gathered by the fore mentioned body.

## Desription
Esentially, the goal of this project is to write a program that takes in a bank card number from the user and outputs whether the card is an American Express, Mastercard, Visa or invalid card  such that American Express is `AMEX`, MasterCard is `MASTERCARD`, Visa is `VISA` and all else is `INVALID`.

To validate a card number, as stated by the problem set, banks use the concept of Luhn's Algorithm to make unique numbers that follow the same system. I cannot imagine how to explain it but, I believe if I demonstrate, it would be easily understood.

#### Luhn's Algorithm
Assume this is the given card number:
```shell
4842347205669802
```
You need to multiply every other number by 2 and then get the sum of the digit of each product. In the case of our number, we would have something like this:
```shell
# Every other number from second last
0 9 6 0 7 3 4 4

# Add digits after multiplying by 2
0 + (1 + 8) + (1 + 2) + 0 + (1 + 4) + 6 + 8 + 8 
```
Thereafter, you add the previously calculated sum to the sum of all the other numbers that were not multiplied.

This should always give you some multiple of 10. If not, the number is deemed invalid. The example number is going to be invalid I just made it up.


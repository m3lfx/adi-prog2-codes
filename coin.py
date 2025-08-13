import random

# The Coin class simulates a coin that can be flipped.

class Coin:

    # The __init__ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):
        self.__sideup = 'Heads'
        self.color = 'silver'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
            
        else:
            self.__sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
        return self.__sideup
    
    def get_color(self):
        return self.color
    
# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = Coin()
    # print(my_coin)
    coin2 = Coin()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin.
    print('I am tossing the coin ...')
    my_coin.toss()

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())
    print(coin2.get_color())

    my_coin.__sideup = 'public property'

    # Display the side of the coin that is facing up.
    print('This side is up:', my_coin.get_sideup())
    print('This side is up coin2:', coin2.get_sideup())

# Call the main function.
main()







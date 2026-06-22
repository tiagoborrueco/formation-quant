"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 6


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    resultat = EXPECTED_BAKE_TIME - elapsed_bake_time
    return resultat

# TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

number_of_layers = 3

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation_time_in_minutes.

    Parameters:
        number_of_layers (int): layer of the lasagna

    Returns:
        int: time needed to confect the lasagna derived from "number of layers"

    Function that takes the number of layers as
    an argument and returns how many minutes il will take to prepare the lasagna
    based on the fact that each layer require 2minutes.
    """
    
    prepa = number_of_layers*2
    return prepa

#TODO (student): define the 'elapsed_time_in_minutes()' function below.
 #TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time): 
    """Calculate the bake time remaining.

    Parameters:
        number_of_layers : nbr of layer of the lasagna
        elapsed_bake_time : time in the oven

    Returns:
        int:  elapsed time from the start of the cooking session.

    Function that takes the actual minutes the lasagna has been in the oven  and the nbr
    of layer of the lasagne as an argument and returns how many has passed from the
    beginning
    """
    perdu = number_of_layers*2 + elapsed_bake_time
    return perdu 
    

# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

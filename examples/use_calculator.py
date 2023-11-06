# examples/use_calculator.py
from simple_calculator.calculator import add, subtract

def main():
    """
     This is the main function of the calculator. It takes two arguments and prints the result of the addition and
    """
    print("Using the calculator to add 5 and 3: ", add(5, 3))
    print("Using the calculator to subtract 3 from 5: ", subtract(5, 3))

# main function for the main module
if __name__ == "__main__":
    main()
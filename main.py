# main.py
from simple_calculator.calculator import subtract, add

def main():
    """
     Subtraction : 5 - 3 Addition : 2 + 3 = 2 - 3 Prints the result
    """
    print("Subtraction: 5 - 3 = ", subtract(5, 3))
    print("Addition: 2 + 3 = ", add(2, 3))

# main function for the main module
if __name__ == "__main__":
    main()
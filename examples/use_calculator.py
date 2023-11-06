# examples/use_calculator.py
from simple_calculator.calculator import add, subtract

def main():
    print("Using the calculator to add 5 and 3: ", add(5, 3))
    print("Using the calculator to subtract 3 from 5: ", subtract(5, 3))

if __name__ == "__main__":
    main()
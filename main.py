# main.py
from simple_calculator.calculator import subtract, add

def main():
    print("Subtraction: 5 - 3 = ", subtract(5, 3))
    print("Addition: 2 + 3 = ", add(2, 3))

if __name__ == "__main__":
    main()
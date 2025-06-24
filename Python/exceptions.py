import sys

try:
    # print(x/y)
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    sys.exit(1)
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)


print(f"{x} / {y} = {result }") #if 'result' in locals() else 'undefined'}")
def factorial(n):
    """
    Calculate the factorial of a number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        print(f"The factorial of {number} is {factorial(number)}")
    except ValueError as e:
        print(e)
    except Exception:
        print("An unexpected error occurred.")

if __name__ == "__main__":
    main()

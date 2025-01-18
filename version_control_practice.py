# factorial.py
def factorial(n):
    """
    Calculate the factorial of a number.
    
    Args:
        n (int): The number to calculate the factorial for.
        
    Returns:
        int: The factorial of the number.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    number = 5
    print(f"The factorial of {number} is {factorial(number)}")

if __name__ == "__main__":
    main()

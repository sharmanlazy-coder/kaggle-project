def divide_numbers(a, b):
    # Check for division by zero and raise a ValueError
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    try:
        print(divide_numbers(10, 0))
    except ValueError as e:
        print(f"Error: {e}")

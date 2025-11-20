def divide_numbers(a, b):
    # This function will crash if b is 0
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    try:
        print(divide_numbers(10, 0))
    except ValueError as e:
        print(f"Error: {e}")

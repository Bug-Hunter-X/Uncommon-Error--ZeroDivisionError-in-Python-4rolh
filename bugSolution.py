def function_with_uncommon_error_solution(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return x + 5
    except ZeroDivisionError:
        return float('inf')  # Handle division by zero
    except Exception as e:
        return f"An unexpected error occurred: {e}"
def function_with_closed_file(filepath):
    try:
        with open(filepath, 'r') as file:
            # ... process the file ...
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    # File automatically closed by with statement
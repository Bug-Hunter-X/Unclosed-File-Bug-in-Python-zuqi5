def function_with_unclosed_file(filepath):
    try:
        file = open(filepath, 'r')
        # ... process the file ...
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    # Missing file.close() call here
def remove_duplicates(numbers):
    unique_numbers = set(numbers)
    return unique_numbers

def filter_greater_than(numbers, threshold):

    filtered_numbers = {num for num in numbers if num > threshold}
    return filtered_numbers

if __name__ == "__main__":
    
    numbers = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1]
    threshold = 2
    
    unique_numbers = remove_duplicates(numbers)
    print("Unique numbers:", unique_numbers)
    
    filtered_numbers = filter_greater_than(numbers, threshold)
    print(f"Numbers greater than {threshold}: {filtered_numbers}")
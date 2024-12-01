def set_operations(set1, set2):
    
    union_set = set1.union(set2)
    
    intersection_set = set1.intersection(set2)
    
    difference_set1_set2 = set1.difference(set2)
    
    symmetric_difference_set = set1.symmetric_difference(set2)
    
    return union_set, intersection_set, difference_set1_set2, symmetric_difference_set

def set_comprehension(numbers):
    
    even_squares = {n**2 for n in numbers if n % 2 == 0}
    
    return even_squares


if __name__ == "__main__":
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    union_set, intersection_set, difference_set, symmetric_difference_set = set_operations(set1, set2)
    
    print("Set Operations:")
    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Difference (set1 - set2):", difference_set)
    print("Symmetric Difference:", symmetric_difference_set)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    even_squares = set_comprehension(numbers)
    
    print("\nSet Comprehension:")
    print("Squares of even numbers:", even_squares)

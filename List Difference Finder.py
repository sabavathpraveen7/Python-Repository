def find_list_difference(list_a, list_b):
    # Subtract set B from set A to find items unique to list A
    difference = list(set(list_a) - set(list_b))
    
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Only in List A: {difference}")
    return difference

# Example usage:
# find_list_difference([10, 20, 30, 40], [20, 40])

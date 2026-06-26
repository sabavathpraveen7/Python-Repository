def reverse_list_manually(original_list):
    reversed_list = []
    # Start index tracking from the very last element
    index = len(original_list) - 1
    
    while index >= 0:
        reversed_list.append(original_list[index])
        index -= 1
        
    print(f"Original List: {original_list}")
    print(f"Reversed List: {reversed_list}")
    return reversed_list

# Example usage:
# reverse_list_manually()
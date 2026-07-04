def dynamic_character_swapper(text):
    # Define a replacement mapping dictionary
    swap_rules = {'a': '4', 'e': '3', 'i': '1', 'o': '0'}
    modified_chars = []
    
    for char in text:
        # Check lowercase version to match easily, keeping original case if not matched
        lower_char = char.lower()
        if lower_char in swap_rules:
            modified_chars.append(swap_rules[lower_char])
        else:
            modified_chars.append(char)
            
    result = "".join(modified_chars)
    print(f"Original: '{text}' -> Swapped: '{result}'")
    return result

# Example usage:
# dynamic_character_swapper("Embedded Logic")
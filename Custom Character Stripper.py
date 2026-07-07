def strip_unwanted_characters(raw_text, characters_to_remove):
    clean_chars = []
    
    for char in raw_text:
        # Only keep the character if it isn't in our removal list
        if char not in characters_to_remove:
            clean_chars.append(char)
            
    result = "".join(clean_chars)
    print(f"Raw:   '{raw_text}'")
    print(f"Clean: '{result}'")
    return result

# Example usage:
# strip_unwanted_characters("Error #404!", ["#", "!"])
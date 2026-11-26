def mask_text(secret_text, visible_chars=4):
    if len(secret_text) <= visible_chars:
        return secret_text
        
    # Calculate how many asterisks are needed and slice the end of the string
    hidden_length = len(secret_text) - visible_chars
    masked_output = ("*" * hidden_length) + secret_text[-visible_chars:]
    
    print(f"Masked Output: {masked_output}")
    return masked_output

# Example usage:
# mask_text("SERIAL-987654321", visible_chars=4)

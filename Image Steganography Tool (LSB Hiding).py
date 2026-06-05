from PIL import Image

def hide_text_in_image(image_path, secret_message, output_path="hidden.png"):
    print(f"Embedding secret message into: {image_path}")
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    
    # Append a delimiter to know where the secret text ends during decoding
    secret_message += "@@"
    # Convert string into a continuous stream of binary bits
    binary_message = "".join(f"{ord(char):08b}" for char in secret_message)
    bit_index = 0
    message_len = len(binary_message)

    width, height = img.size
    for y in range(height):
        for x in range(width):
            if bit_index >= message_len:
                break
                
            r, g, b = pixels[x, y]
            
            # Modify the least significant bit of the red channel if bits remain
            if bit_index < message_len:
                r = (r & 0xFE) | int(binary_message[bit_index])
                bit_index += 1
                
            pixels[x, y] = (r, g, b)
            
    img.save(output_path)
    print(f"✅ Message hidden successfully in: '{output_path}'")

# hide_text_in_image("input_photo.png", "Confidential Hardware Spec v2")
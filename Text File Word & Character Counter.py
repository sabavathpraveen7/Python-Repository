def analyze_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        line_count = len(lines)
        word_count = 0
        char_count_with_spaces = 0
        char_count_no_spaces = 0
        
        for line in lines:
            words = line.split()
            word_count += len(words)
            char_count_with_spaces += len(line)
            char_count_no_spaces += sum(len(word) for word in words)
            
        print(f"--- File Analysis: {filename} ---")
        print(f"Lines:      {line_count}")
        print(f"Words:      {word_count}")
        print(f"Characters (with spaces): {char_count_with_spaces}")
        print(f"Characters (no spaces):   {char_count_no_spaces}")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# analyze_text_file("sample_notes.txt")
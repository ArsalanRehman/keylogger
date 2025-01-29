import re

def translate_keypresses_from_file(file_path):
    # Read the key sequence from the file
    with open(file_path, "r", encoding="utf-8") as file:
        key_sequence = file.read().strip()

    output = []
    buffer = ""
    clipboard = ""  # Stores copied text

    # **Fixed key extraction**
    keys = re.split(r'(\[Key\.[^\]]+\])', key_sequence)  # Keeps both keys and actual text

    i = 0
    while i < len(keys):
        key = keys[i].strip()

        # Debugging log
        # print(f"Processing: {key}")  

        if key.startswith("[Key."):  # It's a special key
            key_name = key[5:-1]  # Remove '[Key.' and ']' to extract key name

            if key_name == "backspace":
                if buffer:
                    buffer = buffer[:-1]  # Remove last typed character
                elif output:
                    output.pop()  # Remove last character from output if buffer is empty
            elif key_name == "enter":
                if buffer:
                    output.append(buffer)
                    buffer = ""
                output.append("\n")  # Preserve new lines
            elif key_name == "space":
                buffer += " "
            elif key_name == "tab":
                buffer += "\t"
            elif key_name == "caps_lock":
                pass  # Ignore caps lock
            elif key_name == "shift":
                pass  # Ignore shift
            elif key_name == "ctrl":
                if i + 1 < len(keys):
                    next_key = keys[i + 1].strip()
                    # print(f"CTRL Key Combo: {next_key}")  # Debugging output
                    if next_key == "[Key.c]":
                        clipboard = buffer if buffer else "".join(output)  # Copy full content
                    elif next_key == "[Key.v]":
                        buffer += clipboard  # Paste clipboard content
                    elif next_key == "[Key.backspace]":
                        buffer = ""  # Ctrl+Backspace clears last word
                    i += 1  # Skip next key since it's part of the combination
            elif key_name == "cmd":
                pass  # Ignore command key
        else:  # It's actual text, append it
            buffer += key
            # print(f"Buffer after adding: {buffer}")  # Debugging statement

        i += 1

    # Append any remaining buffer content
    if buffer:
        output.append(buffer)

    translated_text = "".join(output)
    
    # Debugging output
    print("\n--- FINAL OUTPUT ---\n")
    print(translated_text if translated_text.strip() else "OUTPUT IS BLANK!")

    return translated_text

# File path for the key sequence
file_path = "./keys.txt"

# Translate the key sequence from the file
translated_text = translate_keypresses_from_file(file_path)

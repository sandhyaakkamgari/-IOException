# Attempting to open a non-existent file for reading
try:
    with open("nonexistentfile.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"IOException occurred: {e}")
# Script 1 (create_and_write.py): Creates a file, reopens it, writes content, and saves it.
# Script 2 (read_and_count.py): Opens the existing file and counts the number of characters.

# 1 & 2)
with open("example1.txt", "w") as file:
    pass

with open("example1.txt", "a") as file:
    file.write("Hello, This is 1 line. \n")
    file.write("Hello, This is 2 line. \n")

print("File written successfully.")

with open("example1.txt", "r") as file:
    content = file.read()
    fileCharLen = len(content)

print(f"Number of characters in the file: {fileCharLen}")

# Practice Problems 1, 2, 3
# 1. Word Count (characters + words count karna)
with open("example1.txt", "r") as file:
    content = file.read()
    char_count = len(content)
    word_count = len(content.split())

print(f"Character Count: {char_count}")
print(f"Word Count: {word_count}")

# 2. Append User Input (naya text file mein add karna)
print("Input 3 lines in the file")
lines = []
for idx in range(3):
    line = input(f"Line {idx + 1}: ")
    lines.append(line + "\n")
with open("example1.txt", "a") as file:
    file.writelines(lines)
with open("example1.txt", "r") as file:
    content = file.read()
    new_char_count = len(content)
print(f"Lines appended successfully and calculated the new character count {new_char_count}")

# 3. Line Counter with Keyword (Python word wali lines count karna)
total_lines = 0
python_word_lines = 0
with open("example1.txt", "r") as file:
    for line in file:
        total_lines += 1
        if "Python" in line:
            python_word_lines += 1
print(f"Total Lines: {total_lines}")
print(f"Lines containing 'Python': {python_word_lines}")
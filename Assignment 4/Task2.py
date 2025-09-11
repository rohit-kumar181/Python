try:
    text = input("Enter text to write to the file: ")
    file = open("output.txt", "r+")
    file.write(text + "\n")
    file.close()
    print("Data successfully written to output.txt.\n")

    append_text = input("Enter additional text to append: ")
    file = open("output.txt", "a")
    file.write(append_text + "\n")
    file.close()
    print("Data successfully appended.\n")

    print("Final content of output.txt:")
    file = open("output.txt", "r+")
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
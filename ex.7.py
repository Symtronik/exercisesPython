# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

fileName = input("Filename: ")

fileName = fileName.split(".")

print(f'Extension: {fileName[-1]}')
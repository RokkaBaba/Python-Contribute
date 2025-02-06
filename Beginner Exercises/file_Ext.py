#Write a Python program that accepts a filename from the user and prints the extension of the file.
filename = input("Input the filename:")
f_ext=filename.split(".")
print("The extension of the file is:" + repr(f_ext[-1])) #repr is machine friendly than str


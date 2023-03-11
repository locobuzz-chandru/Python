import os


def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        return "File " + filename + " created successfully."
    except IOError:
        return Exception("Error: could not create file " + filename)


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            return contents
    except IOError:
        return Exception("Error: could not read file " + filename)


def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        return f"Text appended to file {filename} successfully."
    except IOError:
        return Exception("Error: could not append to file " + filename)


def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        return "File " + filename + " renamed to " + new_filename + " successfully."
    except IOError:
        return Exception("Error: could not rename file " + filename)


def delete_file(filename):
    try:
        os.remove(filename)
        return "File " + filename + " deleted successfully."
    except IOError:
        return Exception("Error: could not delete file " + filename)


def create_binary_file():
    try:
        with open("binfile.bin", "wb") as f:
            num = [5, 10, 15, 20, 25]
            arr = bytearray(num)
            f.write(arr)
        return "Binary file created successfully."
    except IOError:
        return Exception("Error: could not create binary file ")


def read_binary_file():
    try:
        with open("binfile.bin", "rb") as f:
            return f.read()
    except IOError:
        return Exception("Error: could not read binary file ")


def read_img():
    try:
        with open("2.png", "rb") as f:
            return f.read()
    except IOError:
        return Exception("Error: could not read binary file ")


if __name__ == '__main__':
    filename1 = "example.txt"
    new_filename = "new_example.txt"

    print(create_file(filename1))
    print(read_file(filename1))
    print(append_file(filename1, "This is some additional text.\n"))
    print(read_file(filename1))
    print(rename_file(filename1, new_filename))
    print(read_file(new_filename))
    print(delete_file(new_filename))
    print(create_binary_file())
    print(read_binary_file())
    print(read_img())
    print(os.getcwd())

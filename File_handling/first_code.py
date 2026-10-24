def openFile():
    # Define the file path (Consider making it a parameter for flexibility)
    filename = "d:\Python_Coding\File_handling\example.txt"
    
    # Open the file in read mode
    file = open(filename, 'r')
    # file variable stores a object
    print(file.read())

    return file
    # The function returns an object for further use.
    
if __name__ == '__main__':
    file = openFile()
    file.close()

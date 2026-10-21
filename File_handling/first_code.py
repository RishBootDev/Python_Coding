def openFile():
    # Define the file path (Consider making it a parameter for flexibility)
    filename = "username.txt"
    
    # Open the file in read mode
    file = open(filename, 'r')
    # file variable stores a object

    return file
    # The function returns an object for further use.
    
if __name__ == '__main__':
    file = openFile()
    file.close()

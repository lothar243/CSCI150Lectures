with open('databaseOutput.txt', 'r') as myfile:

    # Throw away the first three lines
    myfile.readline()
    myfile.readline()
    myfile.readline()
    for line in myfile:
        splitline = [val.strip() for val in line.title().split('|')]
        print("'{} {}':'{}',".format(splitline[1], splitline[2], splitline[3]))

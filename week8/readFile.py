import os

print("Reading dracula.txt, enter q to quit")
progress_file_name = "progress.txt"
# Check to see if a progress file exists. If it does, read the value so we can resume from that line
if os.path.isfile(progress_file_name):
    with open(progress_file_name, "r") as progress_file:
        progress_line = int(progress_file.readline())
else:
    # The progress file didn't previously exist, so start from the beginning
    progress_line = 0

# Open the file to read
with open("dracula.txt", "r") as myfile:
    for line_number, line_text in enumerate(myfile):
        # Fast forward to get to the current_line
        if line_number >= progress_line:
            print(line_text.strip(), end=" ")
        else:
            continue
        # Take some user input, q will quit, all else will advance to next line
        command = input()
        if command == "q":
            # Save the current line to a progress file and quit the program
            print("Quitting at line number {}, we will resume from here next time".format(line_number))
            with open(progress_file_name, "w") as progress_file:
                progress_file.write(str(line_number))

            break



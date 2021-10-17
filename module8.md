# Module 8.1 - The command line

## Why we use the command line

We use the command line interface (CLI) when we want a quick, powerful, text-based interface

Disadvantages (vs using a GUI)

* Initial time to learn
* Less user-friendly
* Intimidating

Advantages (vs using a GUI)

* Less resource intensive for the display
* Remote access
* It doesn't change (You don't have to relearn every 3 years)
* More versatile (You don't have to rely on someone to have implemented something for you)
* Most devices can have a command-line interface
* You look cool (?) run hollywood, or cmatrix

## Terminus Game

[Terminus Game Link](http://web.mit.edu/mprat/Public/web/Terminus/Web/main.html)

In terminus, we have 'Locations'. On a file system, we have directories.

* ls
* cd Location
* cd ..
* cd ~
* less

## Reading and Writing to Files

readDracula.py stages to implement (Practicing incremental development, working toward `readFile.py`

* Display the entire chapter
  * Switch to context manager... with open...
* Display it line-by-line
  * Remove extra whitespace
* Add the ability to quit midway
* Remember the location so that we can resume for next time
  * Switch to enumerate, with line_number and print it out
  * save the value to a file and check that's working
  * open the file, read the number
  * add if statement, show how many times you have to press enter
  * if else: continue
  * point out the error if you just open the file without checking first - check if file exists
* Other additions: the option to delete the progress file and start over
* What happens when we finish reading the chapter/book?

# Module 8.2 ~ More loops

We saw examples of break and continue in the previous example

Nested Loops - a loop within a loop

Introduce .csv files

```bash
more actor.csv # can also demonstrate less, more, cat
column -s, -t actor.csv # to view it in columns
more course_enrollment.csv
cat stolen_gun_data.xlsx | head
```

Start by reading in the csv file into a 2d list

We'll just skip explaining most of this for now - it's just to get a list loaded in to memory

```python
import csv

filename = "actor.csv"

with open(filename, 'r') as myfile:
    csvreader = csv.reader(myfile)

    contents = [row for row in csvreader]

for row in contents:
    print(row)
```

```bash
vim readcsv.py
```

Another nested loop example, this time with a dictionary contains lists as the values

```bash
vim nestedDicts.py
```


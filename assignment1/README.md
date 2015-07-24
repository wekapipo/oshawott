## assignment 1

assignment 1 is to write a program that will:
* take user input
* write some output
* use loops and simple data structures

I will provide an outline for a simple program here. A copy of it will be
pushed to this directory. Just make a copy of it and push the file you make
into the GitHub repo.

### required tools

* [a Git client](https://windows.github.com/)
* [python 3.4](https://www.python.org/downloads/)
  * IDLE (python's integrated development environment, you can run simple
  python commands straight from here, or use file>open to open and edit a
  script. then <F5> to run it.

### resources

* ~~[learn python the hard way](http://learnpythonthehardway.org/book/)~~ is a
really good book that's available online. teachs everything you need to know
* [Dive Into Python 3](http://www.diveinto.org/python3/) is also a good book.
less hands on tho. but still good

### explanation

read the `sample.explained.md`

### goal: part 1

the program, as is, asks the user to input a number of rows and columns they
want. it then creates a table of asterisks based on that size. it then replaces
the top half of the table with numbers.

your goal is instead of that last step with the numbers, to ask for a second
pair of inputs, x and y coordiantes, and replace the asterisk at that location
with another character (whatever you want)

when you are done with this part, save it as a new file and sync with the repo

#### example
```
How many rows do you want: 5
How many cols do you want: 5
Which x coordinate: 1
Which y coordinate: 1
*****
*B***
*****
*****
*****
```

Notice that I we start indexing at 0, so I assumed coordinate (1,1) doesn't
include the first row or column. In most common programming languages list[2]
means the 3rd thing in `list`

### goal: part 2

part two is a bit harder. replace not only the thing at the location the user
specified, but also the cells above, below, and to the left and right of it.

#### example
```
How many rows do you want: 10
How many cols do you want: 10
Which x coordinate: 7
Which y coordinate: 7
**********
**********
**********
**********
**********
*******B**
******BBB*
*******B**
**********
**********

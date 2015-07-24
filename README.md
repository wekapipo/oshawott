##intro

Assignment 1 will introduce you to git, github, and programming [in python]

### git 

git is a [version control
system](https://en.wikipedia.org/wiki/Git_%28software%29), which means it's
software that allows you to track and share changes to code. in git projects
are organized as repos (repositories). a repo is a structure that contains all
the commits (a single object that contains at least one change to one file and a
comment that explains what you changed) and history about them (when they were
pushed, what branch they're from, etc.). A repo can be branched; all the
changes will be done to that *branch* until you decide to merge the branches
back together.

### github

github is a website and community that hosts git repos. Git is a *distributed*
VCS, so your local copy of the repo actually usually contains every single
commit. Any repo can be used as a "central" repo, and even no central repo is
technically necessary. GitHub simply allows you to host a copy of the repo, and
also for you to easily contribute to and share open source projects. Repos can
be set as private but this repo is public ($$$). There's an issue tracker (to
complain about and track problems with the software) as well as a personal wiki
for each repo.There's also some nifty user management and other social features
that GitHub introduces. 

### python

[python](https://en.wikipedia.org/wiki/Python_%28programming_language%29) is a
programming language. it's useful to learn because it's high level (you don't
have to mess with hardware level code), simple (to read, to write), and very
popular. Also [Godot](https://en.wikipedia.org/wiki/Godot_%28game_engine%29) is
a game engine that we might use and it implements its own scripting language
that's based eavily on Python.

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

todo

### goal: part 1

the program, as is, asks the user to input a number of rows and columns they
want. it then creates a table of asterisks based on that size. it then replaces
the top half of the table with numbers.

your goal is instead of that last step with the numbers, to ask for a second
pair of inputs, x and y coordiantes, and replace the asterisk at that location
with another character (whatever you want)

when you are done with this part, sync up the new file into the github repo

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
```

```
The sample code (without the comments, you can read them by opening `setup.py`)
```
def main():

    num_rows = int(input("How many rows do you want: "))
    num_cols = int(input("How many cols do you want: "))

    matrix = []
    for i in range(num_rows):
        matrix.append([])
    for i in range(len(matrix)):
        for j in range(num_cols):
            matrix[i].append('*')

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(j>=i):
                matrix[i][j] = j

    for i in range(len(matrix)):
        for element in matrix[i]:
            print(element, end="")
        print()
        
main()
```
I'll explain segment by segment here:
```
def main():
```
define a `main` function we'll run later

```
    num_rows = ~~int(input("How many rows do you want: "))~~
```
declare a variable num_rows and assign input to it
```
    ~~num_rows = int(~~input("How many rows do you want: ")~~)~~
```
call a function `input`. A function looks like this: `func()` with some
parameters: `func(param1, param2)`. This one has one parameter, a string (of
characters" that represents what the command prompt will say to the user.
Strings are a type of data. Others include `int` (an integer, or number)
`float` (a floating point i.e. decimal number) `char` a character
```
    ~~num_cols = int(~~input("How many cols do you want: ")~~)~~
```
`int()` casts (converts) the parameter into a number. This is important because
by default in Python 3 `input()` returns a string    
```
    matrix = []
```
declare a list named matrix. a list is a datatype that holds other things. in
our case this will be ints
```
    for i in range(num_rows):
```
`for` is a command that loops through a bunch of things. in python it takes the
form of: `for [something] in [list of things]:` in our case our "thing" is `i`
and our "list of things" is `range(num_rows)`: this is another function:
`range([stop])` one that returns a list of numbers. it takes one (or two, but
in this case one) parameter. `range` starts at 0 (by default) and goes until it
hits `stop`. so `range(5)` will make this: `[0,1,2,3,4]`. Which conveniently
contains 5 numers. Why start at 0 and omit the last number rather than start at
1 and include it? In general iterating from 0 turns out to be more useful most
of the time. So get used to counting from zero
```
        matrix.append([])
```
remember that empty list? we'll throw an empty list into it each time we go
through the loop. effect? `matrix` now contains `num_rows` lists. each list
represent a row. clever, huh? notice the `.append()` syntax. append is a
method, which is like a function that doesn't just take a parameter and return
something, but also belongs to something else. in python lists contain a method
`append` 
```
    for i in range(len(matrix)):
        for j in range(num_cols):
            matrix[i].append('*')
```
similar to last time. this time we have nested loops. so run through the first
loop we run through the second loop a bunch of times. notice `matrix[i]`. We're
accessing an element in the matrix list. the `ith` element specifically. notice
we're again counting from 0 (told you that'll come up again). notice also the
`len(matrix)` part. `len()` is a function that returns length. we didn't need
to count the length of the list (since we already had user input) but it's
important to introduce yall to concepts and shit
```
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(j>=i):
                matrix[i][j] = j
```
new structure: `if` statements. `if():` isn't a function, but it sorta looks
like one. it obviously does some check (in this case if the col is equal or
greater to to the row) and only does the next thing if the check passes.
`matrix[i][j] = j` changes the `jth` number in the `ith` list in `matrix` to
`j`
```
    for i in range(len(matrix)):
        for element in matrix[i]:
            print(element, end="")
        print()
```
loops through each element in each row and print it out. notice `print()`'s
interesting syntax. It takes two parameters (in this case). first, the thing to
print out, and second, the `end` parameter. Why this weird `thing="something"`
syntax? Because python allows you to define named parameters. A function
usually has unnamed parameters (that'll you have to insert in order) but python
allows optional and named parameters that let you give the function user the
option to define `end` if and when they want.  
`end` is defaulted to `\n`. that means that usually `print()` will print out
what you want into the console and follow it with a linebreak. since we want
all the elements of a row printed into a line, we override that default
behaviour with an empty string
```
main()
```
finally we call our main function and let it run

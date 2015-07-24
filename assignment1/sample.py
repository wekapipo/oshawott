# define a "main" function that'll we'll run later
#!/usr/bin/python
def main():

    # prompt user for something (and take the result as an int: a number)
    num_rows = int(input("How many rows do you want: "))
    num_cols = int(input("How many cols do you want: "))

    # let's make a table using the inputs as parameters
    matrix = []
    # add 'num_rows' empty rows to 'matrix'
    for i in range(num_rows):
        matrix.append([])
    # add 'num_cols' asteriks to each row
    for i in range(len(matrix)):
        for j in range(num_cols):
            matrix[i].append('*')   # add "*" to the end of the row-list we're on

    # let's change the table
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(j>=i):
                matrix[i][j] = j

    # print everything out
    for i in range(len(matrix)):
        for element in matrix[i]:
            print(element, end="")
        print()

# run that main fuction we defined
main()

def main():


    num_rows = int(input("whats up bro, how many rows u want dawg: "))
    num_cols = int(input("tell me how many columns you too bro: "))

    matrix = []
    
    for i in range(num_rows):
        matrix.append([])

    for i in range(len(matrix)):
            for j in range(num_cols):
                matrix[i].append('*')

    
    print("so homie this is the matrix you wanted: ")
    
    for i in range(len(matrix)):
        for j in range(num_cols):
            print('*', end="")

        print()

    counter = num_cols * num_rows

    while(counter > 0):

        x_cord = int(input("yoo whats the x-cord you want it to be at: "))
        y_cord = int(input("cmon bro you gotta tell me the y-cord too: "))

        #reprompt
        while(x_cord > num_rows -1): 
            x_cord = int(input("yooo you got the wrong x cord, choose a new one: "))
         
        while(y_cord > num_cols -1):
            y_cord = int(input("yooo you got the wrong y cord, choose a new one: "))
        
        #base case
        matrix[y_cord][x_cord] = "X"

        counter -= 1

        if(x_cord == num_rows-1):
            if(matrix[y_cord-1][x_cord] != "X"):
                counter -= 1
            matrix[y_cord-1][x_cord] = "X"
        elif(x_cord == 0):
            if(matrix[y_cord+1][x_cord] != "X"):
                counter -= 1
            matrix[y_cord+1][x_cord] = "X"
        else:
            matrix[y_cord-1][x_cord] = "X"
            matrix[y_cord+1][x_cord] = "X"
            counter -= 2

        if(y_cord == num_cols-1):
            if(matrix[y_cord][x_cord-1] != "X"):
                counter -= 1
            matrix[y_cord][x_cord-1] = "X"
        elif(y_cord == 0):
            if(matrix[y_cord][x_cord+1] != "X"):
                counter -= 1
            matrix[y_cord][x_cord+1] = "X"
        else:
            matrix[y_cord][x_cord-1] = "X"
            matrix[y_cord][x_cord+1] = "X"
            counter -= 2

        print("nice bro, now ur matrix looks like this: ")

        for i in range(len(matrix)):
            for j in range(num_cols):
                print(matrix[i][j], end="")
            print()


    print("Broooo you ran out of spaces to fill. we done here!")

    #matrix[x_cord][y_cord] = "X"
    #matrix[x_cord-1][y_cord] = "X"
    #matrix[x_cord+1][y_cord] = "X"
    #matrix[x_cord][y_cord-1] = "X"
    #matrix[x_cord][y_cord+1] = "X"

#    print("nice bro, now ur matrix looks like this: ")
#
#    for i in range(len(matrix)):
#        for j in range(num_cols):
#            print(matrix[i][j], end="")
#
#        print()


main()

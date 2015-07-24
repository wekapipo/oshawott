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


    x_cord = int(input("yoo whats the x-cord you want it to be at:"))
    y_cord = int(input("cmon bro you gotta tell me the y-cord too"))

    while(x_cord > num_rows -1): 
        x_cord = int(input("yooo you got the wrong x cord, choose a new one: "))
     
    while(y_cord > num_cols -1):
        y_cord = int(input("yooo you got the wrong y cord, choose a new one: "))
    

    matrix[x_cord][y_cord] = "X"
    matrix[x_cord-1][y_cord] = "X"
    matrix[x_cord+1][y_cord] = "X"
    matrix[x_cord][y_cord-1] = "X"
    matrix[x_cord][y_cord+1] = "X"

    print("nice bro, now ur matrix looks like this: ")

    for i in range(len(matrix)):
        for j in range(num_cols):
            print(matrix[i][j], end="")

        print()

main()

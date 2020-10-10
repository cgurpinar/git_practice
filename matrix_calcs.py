from copy import deepcopy
import math

def add_matrix(row):
    temp = [[float(x) for x in input().split()] for _ in range(row)]
    return temp

def sum_matrix(f_matrix, s_matrix):
    f_row, f_col = row_col_matrix(f_matrix)
    s_row, s_col = row_col_matrix(s_matrix)

    sum_matrix = []
    if f_row == s_row and f_col == s_col:
        for i in range(f_row):
            sum_matrix_temp = []
            for j in range(f_col):
                result = f_matrix[i][j] + s_matrix[i][j]
                sum_matrix_temp.append(result)
            sum_matrix.append(sum_matrix_temp)
    else:
        print("The operation cannot be performed.")

    return sum_matrix

def constant_multiply(matrix, multiply):
    row, col = row_col_matrix(matrix)

    temp_matrix = []
    for i in range(row):
        temp = []
        for j in range(col):
            var = matrix[i][j] * multiply
            temp.append(var)               
        temp_matrix.append(temp)
    return temp_matrix

def multiply_matrices(f_matrix, s_matrix):
    f_row, f_col = row_col_matrix(f_matrix)
    s_row, s_col = row_col_matrix(s_matrix)

    if f_col == s_row:
        multiply = []

        for i in range(f_row):
            f_inner = []
            for j in range(s_col):
                s_inner = []
                for k in range(s_row):
                    multi_ = f_matrix[i][k] * s_matrix[k][j]
                    s_inner.append(multi_)
                total = 0
                for s_i in s_inner:
                    total += s_i
                f_inner.append(total)
            multiply.append(f_inner)
    else:
        print("The operation cannot be performed.")

    return multiply

def transposed_main(matrix):
    row, col = row_col_matrix(matrix)

    temp = []
    for i in range(row):
        inner_temp = []
        for j in range(col):
            inner_temp.append(matrix[j][i])
        temp.append(inner_temp)
    
    return temp

def transposed_side(matrix):
    row, col = row_col_matrix(matrix)

    temp = []
    for i in range(row -1, -1, -1):
        inner_temp = []
        for j in range(col -1, -1, -1):
            inner_temp.append(matrix[j][i])
        temp.append(inner_temp)

    return temp

def transposed_vertical(matrix):
    row, col = row_col_matrix(matrix)

    temp = []
    for i in range(row):
        inner_temp = []
        for j in range(col -1, -1, -1):
            inner_temp.append(matrix[i][j])
        temp.append(inner_temp)

    return temp

def transposed_horizontal(matrix):
    row, col = row_col_matrix(matrix)

    temp = []
    for i in range(row-1, -1, -1):
        inner_temp = []
        for j in range(col):
            inner_temp.append(matrix[i][j])
        temp.append(inner_temp)

    return temp

def get_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

def determinant_helper(matrix):
    
    if len(matrix) == 2:                            # base case for a 2x2 matrix
        return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])*1.0
    
    if len(matrix) == 1 and len(matrix[0]) == 1:    # base case for a 1x1 matrix
        return matrix[0][0]*1.0

    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1.0)**c) * matrix[0][c] * determinant_helper(get_minor(matrix, 0, c))
    return determinant

def determinant(matrix):
    det = determinant_helper(matrix)
    return int(det) if det.is_integer() else det

def inverse(matrix):
    det = determinant(matrix)                       # assert determinant != 0, "Matrix does not have an inverse form"
     
    if len(matrix) == 2:                            # base case, for 2x2 matrix
        return [[matrix[1][1]/det, -1*matrix[0][1]/det], [-1*matrix[1][0]/det, matrix[0][0]/det]]
 
    cofactors = []                                  # find matrix of cofactors
    for row in range(len(matrix)):
        cofactor_row = []
        for column in range(len(matrix)):
            minor = get_minor(matrix, row, column)
            cofactor_row.append( truncate(((-1)**(row+column)) * determinant_helper(minor) / det, 3) )
        cofactors.append(cofactor_row)
    cofactors = transposed_main(cofactors)
    return cofactors

def truncate(f, n):                                 # Adjusting decimal points
    if f == 0:
        return 0
    elif f < 0:
        return math.ceil(f * 10 ** n) / 10 ** n
    else:
        return math.floor(f * 10 ** n) / 10 ** n 

def row_col_matrix(matrix):
    row, col = len(matrix), len(matrix[0])
    return row, col

def print_matrix(matrix):
    row, col = row_col_matrix(matrix)

    for i in range(row):
        for j in range(col):
            print(int(matrix[i][j]) if isinstance(matrix[i][j], int) else truncate(matrix[i][j], 3), sep=" ", end=" ")
        print()


exit_ = False

while not exit_:

    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")

    u_choice = input("Your choice: ")

    if u_choice == "0":                 # 0. Exit
        exit_ = True

    elif u_choice == "1":               # 1. Add matrices
        fm_row, fm_col = [int(x) for x in input("Enter size of first matrix: ").split()]
        print("Enter first matrix:")
        f_matrix = add_matrix(fm_row)

        sm_row, sm_col = [int(x) for x in input("Enter size of second matrix: ").split()]
        print("Enter second matrix:")
        s_matrix = add_matrix(sm_row)

        print_matrix(sum_matrix(f_matrix, s_matrix))

    elif u_choice == "2":               # 2. Multiply matrix by a constant
        m_row, m_col = [int(x) for x in input("Enter size of matrix: ").split()]
        print("Enter matrix:") 
        matrix = add_matrix(m_row)

        multi_by = float(input("Enter constant: "))
        print_matrix(constant_multiply(matrix, multi_by))

    elif u_choice == "3":               # 3. Multiply matrices
        fm_row, fm_col = [int(x) for x in input("Enter size of first matrix: ").split()]
        print("Enter first matrix:")
        f_matrix = add_matrix(fm_row)

        sm_row, sm_col = [int(x) for x in input("Enter size of second matrix: ").split()]
        print("Enter second matrix:")
        s_matrix = add_matrix(sm_row)

        print_matrix(multiply_matrices(f_matrix, s_matrix))

    elif u_choice == "4":               # 4. Transpose matrix
        print("\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
        u_choice = input("Your choice: ")

        if u_choice == "1":                     # 4.1. Main diagonal
            m_row, m_col = [int(x) for x in input("Enter size of matrix: ").split()]
            print("Enter matrix:")
            matrix = add_matrix(m_row)

            print_matrix(transposed_main(matrix))

        elif u_choice == "2":                   # 4.2. Side diagonal
            m_row, m_col = [int(x) for x in input("Enter size of matrix: ").split()]
            print("Enter matrix:")
            matrix = add_matrix(m_row)

            print_matrix(transposed_side(matrix))

        elif u_choice == "3":                   # 4.3. Vertical line
            m_row, m_col = [int(x) for x in input("Enter size of matrix: ").split()]
            print("Enter matrix:")
            matrix = add_matrix(m_row)

            print_matrix(transposed_vertical(matrix))
        
        elif u_choice == "4":                   # 4.4. Horizontal line
            m_row, m_col = [int(x) for x in input("Enter size of matrix: ").split()]
            print("Enter matrix:")
            matrix = add_matrix(m_row)

            print_matrix(transposed_horizontal(matrix))
    elif u_choice == "5":               # 5. Calculate a determinant
        m_row, m_col = [int(x) for x in input("Enter size of matrix: ").split()]
        print("Enter matrix:")
        matrix = add_matrix(m_row)

        print(determinant(matrix))

    elif u_choice == "6":               # 6. Inverse matrix  
        m_row, m_col = [int(x) for x in input("Enter size of matrix: ").split()]
        print("Enter matrix:")
        matrix = add_matrix(m_row)

        print_matrix(inverse(matrix))

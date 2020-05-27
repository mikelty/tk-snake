def rotate_matrix(deg, matrix):
    deg = deg % 360
    if deg == 0:
        return matrix
    elif deg == 90:
        return [list(row[::-1]) for row in zip(*matrix)]
    elif deg == 180:
        return [row[::-1] for row in matrix][::-1]
    else:
        return rotate_matrix(90, rotate_matrix(180, matrix))

def check_win()


def sumOfSquares(size, squares):
    result = []

    for _ in range(size):
        sumleft, sumright, square = 0, 0, []

        if size == 1:
            result.append(squares[0][0])

            return result

        firstrow = sum(squares[0])
        lastrow = sum(squares[-1])

        middlerows = squares[1:-1]
        for row in middlerows:
            sumleft += row[0]
            sumright += row[-1]

            square.append(row[1:-1])

        sumtotal = firstrow + sumleft + sumright + lastrow
        result.append(sumtotal)

        squares = square
        size -= 1


sumOfSquares(
    size=3,
    squares=[
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 1],
        [9, 8, 7, 6, 5],
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
    ],
)

sumOfSquares(size=1, squares=[[1]])

sumOfSquares(
    size=4,
    squares=[
        [1, 2, 3, 4, 5, 6, 7],
        [6, 7, 8, 9, 1, 2, 3],
        [2, 3, 4, 5, 6, 7, 1],
        [5, 6, 2, 3, 4, 5, 9],
        [1, 2, 3, 4, 5, 6, 7],
        [6, 7, 8, 9, 1, 2, 3],
        [2, 3, 4, 5, 6, 7, 1],
    ],
)

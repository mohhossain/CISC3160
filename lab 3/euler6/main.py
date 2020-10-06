def challenge():
    sumOfSquares = 0
    squareOfSums = 0
    difference = 0
    for i in range(101):
        sumOfSquares += i ** 2
        squareOfSums += i
    squareOfSums = squareOfSums ** 2
    difference =  squareOfSums - sumOfSquares
    print("The difference between the sum of squares and the square of sums up to 100 is {}".format(difference))

challenge()
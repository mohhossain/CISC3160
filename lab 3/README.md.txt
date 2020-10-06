Euler1 reference:
In order to make this program I need to implement for loop which will run from 1 too 1000 times: for (int i = 1; i < 1000; ++i)
In iteration a conditional statement will check if the number is divisible by 3 and 5: if (i % 3 == 0 && i % 5 == 0)
If the condition is met the number will be added to the sum and keep going until the last number divisible by 3 and 5: sum += i;

Euler1 psuedo code: 

sum = 0

for i from 0 to 1000 
	if i divisible by 3 and 5
		sum = sum + i
print sum


Euler6 reference: 
I will need to implement a for loop which will run from 1 to 100 times: for i in range(101):
In each iteration each number will be squared and added to the sum of squares: sumOfSquares += i ** 2
Also, in each iteration each numbers will be added to the square of sums: squareOfSums += i
After the for loop the square of sums will be squared: squareOfSums = squareOfSums ** 2
Then we can find the difference by substracting the sum of squares from square of sums: difference =  squareOfSums - sumOfSquares

Euler6 psuedo code:

sum of squares = 0
square of sums = 0
difference = 0

for i from 0 to 100

	sum of squares =  i ** 2 + sum of squares
	square of sums = i + square of sums

square of sums = square of sums ** 2
differnce = square of sums - sum of squares

print difference
	



Challenge
Inspired by this tweet, today's challenge is to calculate the additive persistence of a number, defined as how many loops you have to do summing its digits until you get a single digit number. Take an integer N:

Add its digits

Repeat until the result has 1 digit

The total number of iterations is the additive persistence of N.

Your challenge today is to implement a function that calculates the additive persistence of a number.

Look at the input on Github here.

Example 1
input = 13 output = 1

Explained:

Given 13, sum the digits 1 and 3 to get 4.

4 is a single digit number. We're done

Example 2
input = 1234 output = 2

Explained:

Given 1234, sum the digits 1, 2, 3 and 4 to get 10.

Given 10, sum the digits 1 and 0 to get 1.

1 is a single digit number. We're done

Example 3
input = 9876 output = 2

Explained:

Given 9876, sum the digits 9, 8, 7 and 6 to get 30.

Given 30, sum the digits 3 and 0 to get 3.

3 is a single digit number. We're done

Example 4
input = 199 output = 3

Explained:

Given 199, sum the digits 1, 9 and 9 to get 19.

Given 19, sum the digits 1 and 9 to get 10.

Given 10, sum the digits 1 and 0 to get 1.

1 is a single digit number. We're done
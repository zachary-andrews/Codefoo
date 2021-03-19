Challenge
Alright ladies and bois, I got some moldy fruit in my house. Help me out.

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

Example 1
See a visual example here

Input: [[2,1,1],[1,1,0],[0,1,1]]

Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]

Output: -1

Example 3:

Input: [[0,2]]

Output: 0

Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Acknowledgement
This challenge was taken from Leet Code. Feel free to leverage Leet Code and their structures of the data to make it easier to focus on your algorithm.
Challenge
There is a light in a room which lights up only when someone is in the room (think motion detector). You are given a set of intervals in entrance and exit times as single integers, and expected to find how long the light has been on. When the times overlap, you need to find the time between the smallest and the biggest numbers in that interval.

You'll be given a set of two integers per line telling you the time points that someone entered and exited the room, respectively. Each line is a visitor, each block is a room. Example:

1 3
2 3
4 5
Your program should report the number of hours the lights would be on. From the above example:

3
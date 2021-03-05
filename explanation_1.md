# Finding the Square Root of an Integer

Given a positive number, we have to find the square root of it (without libraries) and also return the floor value of the square root.


Thanks to the help of a binary seach algorithm, the time complexity of this solution is O(log(n)). I initialized the start and the end, then compared the square of the middle integer with the number provided.
If it's equal - we found the square root. If not we look left and right depending on if the square is greater or smaller than the number.
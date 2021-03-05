Search in a Rotated Sorted Array

We have to find a way to find an element in a rotated array in O(log n) time.
In order to achieve this I used a binary search recursively.
First by finding the middle point. If the mid point is the number to search for, return the mid point.
Else update the low and high and recur until the number is found
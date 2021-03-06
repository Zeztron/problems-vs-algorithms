'''
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4


'''

def rotated_array_search(input_list, low, high, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), low(num), high(num), number(int): Input array to search, first and last number,  and the target
    Returns:
       int: Index or -1
    """

    if low > high:
      return -1
  
    
    midpoint = (low + high) // 2
    if input_list[midpoint] == number:
      return midpoint
    
    if input_list[low] <= input_list[midpoint]:

      if number >= input_list[low] and number <= input_list[midpoint]:
        return rotated_array_search(input_list, low, midpoint - 1, number)
      
      return rotated_array_search(input_list, midpoint + 1, high, number)
    
    if number >= input_list[midpoint] and number <= input_list[high]:
      return rotated_array_search(input_list, midpoint + 1, high, number)
    
    return rotated_array_search(input_list, low, midpoint - 1, number)

    

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, 0, len(input_list) - 1, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

'''
  Finding the Square Root of an Integer

  Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

  For example if the given number is 16, then the answer would be 4.

  If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

  The expected time complexity is O(log(n))

'''


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """



    # Return the number if the input is 0 or 1 (Base case)
    if (number == 0 or number == 1):
      return number
    
    # Variable ot store the final result
    square_root = 0

    # Initialize the start and end
    start = 1
    end = number // 2

    while start <= end:

      # Grab the middle integer and then square it
      middle = (start + end) // 2
      square = middle * middle


      # Compare the square with the given number
      # And decide whether to return it or adjust start and end
      if square == number:
        return middle
      elif square < number:
        start = middle + 1
        square_root = middle
      else:
        end = middle - 1
    
    return square_root

    
    
    


  
    

    
   


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

#create a function that takes a list of numbers and returns the sum of those numbers.
"""def sum_of_numbers(numbers):
    return sum(numbers)

#test the function

print(sum_of_numbers([1, 2, 3, 4, 5])) """
# #should return 15

# create a function that takes a list of numbers and returns the sum of those numbers.
def sum_of_numbers(numbers: list[float]) -> float:
    """Return the sum of the given numeric list."""
    return sum(numbers)

def average_of_numbers(numbers: list[float]) -> float:
    """Return the arithmetic mean of the given numeric list.
    
    Raises:
        ValueError: if `numbers` is empty.
    """
    if not numbers:
        raise ValueError("average_of_numbers() requires a non-empty list")
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(sum_of_numbers(nums))       # should print 15
    print(average_of_numbers(nums))   # should print 3.0
def sum_nested_list(nested_list):
    """
    Calculate the sum of all numbers in a nested list.
    This function takes a list that may contain integers and other nested lists.
    It recursively traverses the list and sums all the integers, no matter how deeply nested they are.

    Args:
        nested_list (list): A list that may contain integers or other lists of integers.

    Returns:
        int: The total sum of all integers in the nested list, including those in sublists.
    """
    total = 0
    for element in nested_list:
        if isinstance(element, list):  
            total += sum_nested_list(element) 
        else:
            total += element  
    return total
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
result = sum_nested_list(nested_list)
print("The total sum of the nested list is:", result)

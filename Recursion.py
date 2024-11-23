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
#Task2
def calculate_directory_size(directory):
    total_size = 0
    for key, value in directory.items():
        if isinstance(value, int):
            total_size += value
        elif isinstance(value, dict):
            total_size += calculate_directory_size(value)
    return total_size
    print("/n")
#Task2
directory_structure = {
    "file1.txt": 200,
    "file2.txt": 300,
    "subdir1": {
        "file3.txt": 400,
        "file4.txt": 100
    },
    "subdir2": {
        "subsubdir1": {
            "file5.txt": 250
        },
       "file6.txt": 150
    }
}
print("Total size of the directory:", calculate_directory_size(directory_structure))

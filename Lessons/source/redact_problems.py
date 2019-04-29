#!python

def redact_lists(arrayOne, arrayTwo):
    # Create an empty list to put the values of the new array in
    # Put arrayTwo as a set
    # Iterate through the list of arrayOne
    # Check if the element is not in arrayTwo
    # Append that output into my empty array
    # Output that new array

    result_set = []
    filtered_words = set(arrayTwo)
    for element in arrayOne:
        if element not in filtered_words:
            result_set.append(element)         
    return result_set
    

print(redact_lists(['A', 'B', 'C'], ['C', 'D', 'E']))

def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    result_list = list2
    # Followed by the elements of list1 in reverse order
    list1.reverse()

    result_list.extend(list1)
    return result_list
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

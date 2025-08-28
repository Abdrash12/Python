#lists
test_list = [1,2,3,4,5,6,7,8,9,10]
test_list.append(11)
print("Appended List: ", test_list)
test_list.extend([12,13,14,15])
print("Extended List: ", test_list)
test_list.reverse()
print("Reversed List: ", test_list)
test_list.sort()
print("Sorted List: ", test_list)
print("The number of times 11 appears in the list is" ,test_list.count(11))
print("The length of the list is: ", len(test_list))
test_list.insert(14,16)
print("List after inserting 16 at index 14: ", test_list)
print("The value at index 4 is: ", test_list.index(4))
print("Does 4 exist in the list?", 4 in test_list)
test_list.pop()
print("List after popping the last element: ", test_list)
test_list.remove(7)
print("List after removing 7: ", test_list)



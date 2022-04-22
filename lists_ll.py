
#todo - Section barrier
#! - Title of section
#& - Lesson information
#^ - Notices
#? - Notes
#* - Lesson examples and outputs
#~ - Instructions work

#todo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#! Working with Lists

#& Now that we know how to create and access list data, we can start to explore additional ways of working with lists.
#& In this lesson, you’ll learn how to:
#^ Add and remove items from a list using a specific index.
#^ Create lists with continuous values.
#^ Get the length of a list.
#^ Select portions of a list (called slicing).
#^ Count the number of times that an element appears in a list.
#^ Sort a list of items.
#? Note: In some of the exercises, we will be using built-in functions in Python. If you haven’t yet explored the concept of a function, it may look a bit new. Below we compare it to the method syntax we learned in the earlier lesson.
#& Here is a preview:
#& # Example syntax for methods
#* list.method(input)
#& # Example syntax for a built-in function 
#* builtinfuncion(input)


#?          Python list methods
#? .count() - A list method to count the number of occurances of an element in a list.
#? .insert() - A list method to insert an element into a specific index of a list.
#? .pop() - A list method to remove an element from a specific index or from the end of a list.
#? range() - A built-in Python function to create a sequence of integers.
#? len() - A built-in Python function to to get the length of a list.
#? .sort() / sorted() - A method and a built-in function to sort a list.


#! Adding by Index: Insert

#& The Python list method .insert() allows us to add an element to a specific index in a list.
#& The .insert() method takes in two inputs:
#^ The index you want to insert into.
#^ The element you want to insert at the specified index.
#^ The .insert() method will handle shifting over elements and can be used with negative indices.
#& To see it in action let’s imagine we have a list representing a line at a store:
#* store_line = ["Karla", "Maxium", "Martim", "Isabella"]
#& "Maxium" saved a spot for his friend "Vikor" and we need to adjust the list to add him into the line right behind "Maxium".
#& For this example, we can assume that "Karla" is the front of the line and the rest of the elements are behind her.
#& Here is how we would use the .insert() method to insert "Vikor" :
#* store_line.insert(2, "Vikor")
#* print(store_line) 
#& Would output:
#* ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']
#? Some important things to note:
#& The order and number of the inputs is important. The .insert() method expects two inputs, the first being a numerical index, followed by any value as the second input.
#& When we insert an element into a list, all elements from the specified index and up to the last index are shifted one index to the right. This does not apply to inserting an element to the very end of a list as it will simply add an additional index and no other elements will need to shift.

#~ 1
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

#~ 2
front_display_list.insert(0, "Pineapple")
print(front_display_list)

#todo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#! Removing by Index: Pop

#& Just as we learned to insert elements at specific indices, Python gives us a method to remove elements at a specific index using a method called .pop().
#& The .pop() method takes an optional single input:
#^ The index for the element you want to remove.
#& To see it in action, let’s consider a list called cs_topics that stores a collection of topics one might study in a computer science program.
#* cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
#& Two of these topics don’t look like they belong, let’s see how we remove them using .pop().
#& First let’s remove "Clowns 101":
#* removed_element = cs_topics.pop()
#* print(cs_topics)
#* print(removed_element)
#& Would output:
#* ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
#* 'Clowns 101'
#& Notice two things about this example:
#^ The method can be called without a specific index. Using .pop() without an index will remove whatever the last element of the list is. In our case "Clowns 101" gets removed.
#^ .pop() is unique in that it will return the value that was removed. If we wanted to know what element was deleted, simply assign a variable to the call of the .pop() method. In this case, we assigned it to removed_element.
#& Lastly let’s remove "Balloon Making":
#* cs_topics.pop(2)
#* print(cs_topics)
#& Would output:
#* ['Python', 'Data Structures', 'Algorithms']
#& Notice two things about this example:
#^ The method can be called with an optional specific index to remove. In our case, the index 2 removes the value of "Balloon Making".
#^ We don’t have to save the removed value to any variable if we don’t care to use it later.
#? Note: Passing in an index that does not exist or calling .pop() on an empty list will both result in an IndexError.

#~ 1
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

#~ 2
data_science_topics.pop()
print(data_science_topics)

#~ 3
data_science_topics.pop(3)
print(data_science_topics)

#todo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#! Consecutive Lists: Range

#& Often, we want to create a list of consecutive numbers in our programs. For example, suppose we want a list containing the numbers 0 through 9:
#* my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#& Typing out all of those numbers takes time and the more numbers we type, the more likely it is that we have a typo that can cause an error.
#& Python gives us an easy way of creating these types of lists using a built-in function called range().
#& The function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input.
#& So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:
#* my_range = range(10)
#* print(my_range)
#& Would output:
#* range(0, 10)
#^ Notice something different? The range() function is unique in that it creates a range object. It is not a typical list like the ones we have been working with.
#& In order to use this object as a list, we have to first convert it using another built-in function called list().
#& The list() function takes in a single input for the object you want to convert.
#& We use the list() function on our range object like this:
#* print(list(my_range))
#& Would output:
#* [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#~ 1
number_list = range(9)
print(list(number_list))

#~ 2
zero_to_seven = range(8)
print(list(zero_to_seven))

#todo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#! The Power of Range!

#& By default, range() creates a list starting at 0. However, if we call range() with two inputs, we can create a list that starts at a different number.
#& For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):
#* my_list = range(2, 9)
#* print(list(my_list))
#& Would output:
#* [2, 3, 4, 5, 6, 7, 8]
#& If we use a third input, we can create a list that “skips” numbers.
#& For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:
#* my_range2 = range(2, 9, 2)
#* print(list(my_range2))
#& Would output:
#* [2, 4, 6, 8]
#& We can skip as many numbers as we want!
#& For example, we’ll start at 1 and skip in increments of 10 between each number until we get to 100:
#* my_range3 = range(1, 100, 10)
#* print(list(my_range3))
#& Would output:
#* [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
#& Our list stops at 91 because the next number in the sequence would be 101, which is greater than 100 (our stopping point).

#~ 1
range_five_three = range(5, 15, 3)

#~ 2
range_diff_five = range(0, 40, 5)

#todo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#! Length

#& Often, we’ll need to find the number of items in a list, usually called its length.
#& We can do this using a built-in function called len().
#& When we apply len() to a list, we get the number of elements in that list:
#* my_list = [1, 2, 3, 4, 5]
#* print(len(my_list))
#& Would output:
#* 5

#~ 1
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
big_range = range(2, 3000, 10)
# Your code below: 
long_list_len = len(long_list)

#~ 2
print(long_list_len)

#~ 3
big_range_length = len(big_range)

#~ 4
print(big_range_length)

#~ 5
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
big_range = range(2, 3000, 100)
# Your code below: 
long_list_len = len(long_list)
print(long_list_len)
big_range_length = len(big_range)
print(big_range_length)

#todo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#! Slicing Lists I

#& In Python, often we want to extract only a portion of a list. Dividing a list in such a manner is referred to as slicing.
#& Lets assume we have a list of letters:
#* letters = ["a", "b", "c", "d", "e", "f", "g"]
#& Suppose we want to select from "b" through "f".
#& We can do this using the following syntax: letters[start:end], where:
#^ start is the index of the first element that we want to include in our selection. In this case, we want to start at "b", which has index 1.
#^ end is the index of one more than the last index that we want to include. The last element we want is "f", which has index 5, so end needs to be 6.
#* sliced_list = letters[1:6]
#* print(sliced_list)
#& Would output:
#* ["b", "c", "d", "e", "f"]
#? Notice that the element at index 6 (which is "g") is not included in our selection.

#~ 1
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:4]
# Your code below: 
print(beginning)

#~ 2
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:2]
# Your code below: 
print(beginning)

#~ 3
middle = suitcase[2:4]
print(middle)

#todo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#! Slicing Lists II

#& Slicing syntax in Python is very flexible. Let’s look at a few more problems we can tackle with slicing.
#& Take the list fruits as our example:
#* fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
#& If we want to select the first n elements of a list, we could use the following code:
#* fruits[:n]
#& For our fruits list, suppose we wanted to slice the first three elements.
#& The following code would start slicing from index 0 and up to index 3. Note that the fruit at index 3 (orange) is not included in the results.
#* print(fruits[:3])
#& Would output:
#* ['apple', 'cherry', 'pineapple']
#& We can do something similar when we want to slice the last n elements in a list:
#* fruits[-n:]
#& For our fruits list, suppose we wanted to slice the last two elements.
#& This code slices from the element at index -2 up through the last index.
#* print(fruits[-2:])
#& Would output:
#* ['orange', 'mango']
#& Negative indices can also accomplish taking all but n last elements of a list.
#* fruits[:-n]
#& For our fruits example, suppose we wanted to slice all but the last element from the list.
#& This example starts counting from the 0 index up to the element at index -1.
#* print(fruits[:-1])
#& Would output:
#* ['apple', 'cherry', 'pineapple', 'orange']

#~ 1
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
# Your code below: 
last_two_elements = suitcase[-2:]
print(last_two_elements)

#~ 2
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)


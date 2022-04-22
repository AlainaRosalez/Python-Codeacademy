
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


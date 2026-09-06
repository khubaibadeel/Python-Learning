
# List:-
    # "List is a data structure in Python used to store multiple Pieces of Data in a specific Sequence."
    # --> Each piece of Data is known as Item/Element.


# List Creation:-
fruits =["Mango", "StrawBerry", "Grapes", "Apple", "Banana"] # List created
print(fruits)   #  printed the list


# List Properties:-
#    --> Dynamic Size:
#               The List in Python can change its size. U add/remove items without any problem. List automatically Adjusts its Size.

#    --> Index-Based Access:
#               Every item in a list has a position called index. First has 0, second has 1 and so on. These index can be used to get a specific item from the list.

#    --> Ordered Collection:
#               The order in which you add items to the list is preserved. Each time u append a new item it gets its new order/index automatically.



# List Operations:-
#    1. Insertion: U can insert an item at different positions in a list using insert() function.

students =["Khubaib", "Ahmed", "Ali", "Usman", "Bilal"]
students.insert(0,"Sample")
print(students) # ['Sample', 'Khubaib', 'Ahmed', 'Ali', 'Usman', 'Bilal']


#    2. Deletion:
#           i) Removing by Value:
students.remove("Sample")
print(students)
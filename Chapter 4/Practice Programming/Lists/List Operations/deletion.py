#    2. Deletion:
#           i) Removing by Value:
#                   Use remove() function to remove the occurence of an element.
students =["Khubaib", "Ahmed", "Ali", "Usman", "Bilal"]
students.remove("Khubaib")
print(students)     # ['Ahmed', 'Ali', 'Usman', 'Bilal']

#           ii) Removing by Index:
#                   Use pop() function along with the specific index of the element to be removed. 
subjects = ["English", "Urdu", "Math", "CS", "Physics", "Islamiat"] 
subjects.pop(3)    # Removed "CS" from the list.
print(subjects)    #['English', 'Urdu', 'Math', 'Physics', 'Islamiat']

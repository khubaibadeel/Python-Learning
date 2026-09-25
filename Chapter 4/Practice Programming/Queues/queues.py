from queue import Queue

queue = Queue()

queue.put("khubaib")
queue.put("adeel")

person=queue.get()
print(person)

person=queue.get()
print(person)

################################################################################
# queue.py
#
# Programmeren 2
#
# Rivka Vollebregt
# 12164968
#
# Implements a queue


class Queue:

    def __init__(self):
        self._data = []

    # add element to back of queue
    def enqueue(self, element):
        self._data.append(element)

    # returns the size of the list with data
    def size(self):
        return len(self._data)

    # remove and return element from front of queue
    def dequeue(self):
        #assert self.size() > 0
        return self._data.pop(0)

    # print the frontmost element
    def top(self):
        return self._data[-1]

    # empties list
    def empty(self):
        return self._data.clear()


q = Queue()          # create new queue
q.enqueue(3)         # add number 3 to back of queue
q.enqueue(1)         # add number 1 to back of queue
print(q.dequeue())   # prints first number "in", so 3
print(q.top())       # prints the frontmost element in the queue
print(q.size())      # prints the number of elements still waiting in the queue
print(q.empty())     # empties list and prints result

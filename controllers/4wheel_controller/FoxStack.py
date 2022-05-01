"""####################################################
A Stack class
Susan Fox
Spring 2007
Revised Spring 2014 to update style."""

class Stack:
    """A stack is a linear collection used to hold qData that is waiting
    for some purpose.  Values are added at one end and removed from the
    same end, like a stack of plates"""

    def __init__(self, vallist=[]):
        """When creating a new stack, you can give a list of values to
        insert in the stack at the start.  The front of the list becomes
        the top of the stack."""
        self.data = vallist[:]
        self.size = len(self.data)


    def isEmpty(self):
        """Returns true if the stack is empty, or false otherwise."""
        return self.size == 0


    def firstElement(self):
        """Another name for top"""
        return self.top()


    def top(self):
        """Returns the first value in the stack, without removing it."""
        if self.isEmpty():
            return None
        else:
            return self.data[0]


    def insert(self, val):
        """Inserts a new value at the end of the stack."""
        self.data.insert(0,val)
        self.size = self.size + 1 

    def push(self, val):
        """Another name for inserting"""
        self.insert(val)


    def delete(self):
        """Removes the first element from the stack, returning its value."""
        first = self.data[0]
        self.data.pop(0)
        self.size = self.size - 1
        return first

    def pop(self):
        """Another name for deleting"""
        return self.delete()


    def findMatch(self, value, comparer):
        """Given a value, and a function to use for comparing values, it searches the queue for a
        matching value, returning it if found, or returning False if not found"""
        foundInd = self._matchIndex(value, comparer)
        if foundInd == -1:
            return False
        else:
            return self.data[foundInd]


    def _matchIndex(self, value, comparer):
        """Given a value, and a function to use for comparing values, it searches the queue for a
        matching value, returning its index position if found, or False if not found"""
        for i in range(self.size):
            nextNode = self.data[i]
            if comparer(value, nextNode):
                return i
        return -1


        
    def __str__(self):
        """Creates a string containing the qData, just for debugging."""
        stackStr = "Stack: <- "
        if self.size <= 3:
            for val in self.data:
                stackStr = stackStr + str(val) + " "
        else:
            for i in range(3):
                stackStr = stackStr + str(self.data[i]) + " "
            stackStr = stackStr + "..."
        stackStr = stackStr + "]"
        return stackStr
# end class Stack


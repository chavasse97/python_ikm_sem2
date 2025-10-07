class MyStack:
        def __init__(self):
            self._data = []

        def push(self, item):
            self.add = [item]
            self._data += self.add

        def size(self):
            self.length = 0
            for self.item in self._data:
               self.length += 1
            return self.length

        def last(self):
           return self._data[-1]
        
        def pop(self):
           self.element = self._data[-1]
           del self._data[-1]
           return self.element
        
        def clear(self):
           self._data = []
           return self._data

def Command(command, *args):
    if command == "size":
        print("size =", stack.size())
    elif command == "back":
      try:  
        print("Last element =", stack.last())
      except IndexError:
        print('IndexError: a stack has no elements')
    elif command == "pop":
      try:
        print("Element deleted:", stack.pop())
      except IndexError:
        print('IndexError: a stack has no elements')
    elif command == "clear":
        stack.clear()
        print("ok")
    elif command == "push":
      try:
        stack.push(int(args[0]))
        print("ok")
      except ValueError:
        print('ValueError: an element "', args[0], '" is not a number')
      except IndexError:
        print('IndexError: input an element')
    elif command == "exit":
        print("bye")
    elif command == "help":
       print("push n - adds new element(n) to the stack")
       print("size - shows a size of the stack")
       print("back - shows a last element of the stack")
       print("pop - deletes a last element of the stack")
       print("clear - deletes all elements in the stack")
       print("exit - ends the program")
    else:
       print('Command "', command, '" does not exist')
       print('Type "help" to see available commands')


stack = MyStack()
while True:
    print("Input a command:", end=' ')
    command, *args = input().split()
    Command(command, *args)
    if command == "exit":
      break

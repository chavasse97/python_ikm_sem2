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
        print(stack.size())
    elif command == "back":
      try:  
        print(stack.last())
      except IndexError:
        print('index error(a stack has no elements)')
    elif command == "pop":
      try:
        print(stack.pop())
      except IndexError:
        print('index error(a stack has no elements)')
    elif command == "clear":
        stack.clear()
        print("ok")
    elif command == "push":
      try:
        stack.push(int(args[0]))
        print("ok")
      except ValueError:
        print('value error(an element "', args[0], '" is not a number)')
      except IndexError:
        print('index error(input an element)')
    elif command == "exit":
        print("bye")
    else:
       print('command "', command, '" does not exist')


stack = MyStack()
while True:
    command, *args = input().split()
    Command(command, *args)
    if command == "exit":
      break
